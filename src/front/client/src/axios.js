import axios from 'axios';

const HTTP = axios.create({
  baseURL: 'http://api.wastecation.ru/client/',
});

export default HTTP;
