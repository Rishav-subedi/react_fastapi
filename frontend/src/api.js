import axios from 'axios';

//Create an Instance of axios with the base URL
const api = axios.create({
    baseURL: "http://localhost:8000"
});

export default api;
