import axios from 'axios';

const HTTP = axios.create({
  baseURL: '/api/client/',
});

export default HTTP;
