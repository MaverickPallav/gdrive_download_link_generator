const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const path = require('path');

let mainWindow;

app.whenReady().then(() => {
    // Start the Streamlit server
    exec('bash run_streamlit.sh', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error starting Streamlit: ${error.message}`);
            return;
        }
        console.log(`Streamlit output: ${stdout}`);
    });

    // Create the Electron window
    mainWindow = new BrowserWindow({
        width: 1280,
        height: 800,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    // Load the Streamlit app from localhost
    mainWindow.loadURL('http://localhost:8501');

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
