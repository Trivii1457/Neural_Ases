import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Cambiar según la configuración del backend

export const uploadAudio = async (audioFile) => {
    const formData = new FormData();
    formData.append('audio', audioFile);

    try {
        const response = await axios.post(`${API_URL}/api/reports/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error uploading audio:', error);
        throw error;
    }
};

export const generateReport = async (audioId) => {
    try {
        const response = await axios.post(`${API_URL}/api/reports/generate`, { audioId });
        return response.data;
    } catch (error) {
        console.error('Error generating report:', error);
        throw error;
    }
};

export const downloadReport = async (reportId) => {
    try {
        const response = await axios.get(`${API_URL}/api/reports/download/${reportId}`, {
            responseType: 'blob',
        });
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'report.pdf'); // Nombre del archivo a descargar
        document.body.appendChild(link);
        link.click();
    } catch (error) {
        console.error('Error downloading report:', error);
        throw error;
    }
};