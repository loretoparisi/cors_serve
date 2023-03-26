/**
 * Main Thread
 */
const newWorker = new Worker('worker.js');
const buffMemLength = new SharedArrayBuffer(1024); //byte length
var typedArr = new Int16Array(buffMemLength);
//original data
typedArr[0] = 20;
//sending the buffer to worker 
newWorker.postMessage(buffMemLength);

//onmessage event
newWorker.onmessage = (e) => {
    console.log('[the main thread]');
    console.log(`Data updated from the worker thread: ${typedArr[0]}`);
}