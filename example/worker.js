/**
 * Worker Thread
 */
let BYTE_PER_LENTH = 5;
addEventListener('message', ({ data }) => {
    var arr = new Int16Array(data);

    console.log('[worker thread]');
    console.log(`Data received from main thread ${arr[0]}`);
    
    //updating the data from the worker thread 
    let dataChanged = 5 * BYTE_PER_LENTH;
    arr[0] = dataChanged;
    //Sending to the main thread 
    postMessage('Updated');
})