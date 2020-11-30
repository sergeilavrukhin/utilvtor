import axios from 'axios';

const token = localStorage.getItem('token');
const bearer = `Bearer ${token}`;

const HTTP_TOKEN = axios.create({
  baseURL: 'http://api.wastecation.ru/client/',
  headers: {
    Authorization: bearer,
  },
});

export default HTTP_TOKEN;
