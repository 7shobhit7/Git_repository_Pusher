document.getElementById('githubForm').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent the default form submission

    const username = document.getElementById('githubUsername').value;
    const repoName = document.getElementById('githubRepo').value;
    const githubToken = document.getElementById('githubToken').value;
    const videoFile = document.getElementById('videoFile').files[0];

    if (!videoFile) {
        alert('Please select a video file.');
        return;
    }

    // Display a status message
    document.getElementById('status').innerHTML = 'Uploading and processing video...';

    // Create a FormData object to send the file to the server
    const formData = new FormData();
    formData.append('videoFile', videoFile);








    // Add this code where you want to trigger the execution of ex.py
    setTimeout(function () {
    // Send a request to run_ex endpoint to execute ex.py
    fetch('/run_ex', {
        method: 'POST',
    })
    .then(function (response) {
        if (response.ok) {
            // Execution started successfully
            console.log('Execution started successfully.');
        } else {
            // Handle errors here
            console.error('Execution failed.');
        }
    })
    .catch(function (error) {
        // Handle network or other errors here
        console.error('An error occurred.', error);
    });
        }, 5000); // Delay execution by 5 seconds (5000 milliseconds)










    

    try {

        // Send the video file to the server for processing
        const response = await fetch('/process_video', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const responseData = await response.json();
            // Update the status div with a success message or result
            document.getElementById('status').innerHTML = responseData.message;
        } else {
            // Handle errors here
            document.getElementById('status').innerHTML = 'Video processing failed.';
        }
    } catch (error) {
        // Handle network or other errors here
        document.getElementById('status').innerHTML = 'An error occurred.';
    }
});
