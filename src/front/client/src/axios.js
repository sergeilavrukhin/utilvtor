import axios from 'axios';

const HTTP = axios.create({
  baseURL: 'https://www.wastecation.ru/api/client/',
});

export default HTTP;
