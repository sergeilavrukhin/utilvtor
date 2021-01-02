<!DOCTYPE html>
<html lang="ru">
<head>
  <title>Веботход.ру</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, maximum-scale = 1, minimum-scale = 1">
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
        font-size: 1rem;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: left;
    }
    .container, .container-fluid, .container-sm, .container-md, .container-lg, .container-xl {
        max-width: 1140px;
        padding-right: 15px;
        padding-left: 15px;
        margin-right: auto;
        margin-left: auto;
    }
    .row {
        display: flex;
        flex-wrap: wrap;
        margin-right: -15px;
        margin-left: -15px;
    }
    .m-1 {
        margin: 0.25rem !important;
    }
    .mb-3, .my-3 {
        margin-bottom: 1rem !important;
    }
    .mt-3, .my-3 {
        margin-top: 1rem !important;
    }
    .card {
        position: relative;
        display: flex;
        flex-direction: column;
        min-width: 0;
        word-wrap: break-word;
        background-color: #fff;
        background-clip: border-box;
        border: 1px solid rgba(0, 0, 0, 0.125);
        border-radius: 0.25rem;
    }
    .card-body {
        flex: 1 1 auto;
        min-height: 1px;
        padding: 1.25rem;
    }
    .card {
        word-wrap: break-word;
    }
    .p-4 {
    padding: 1.5rem !important;
    }
    .bg-light {
        background-color: #f8f9fa !important;
    }
    .col-md-4 {
        flex: 0 0 33.333333%;
        max-width: 33.333333%;
    }
    .col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col, .col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm, .col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md, .col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg, .col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl, .col-xl-auto {
        position: relative;
        width: 100%;
        padding-right: 15px;
        padding-left: 15px;
    }
    .text-success {
        color: #28a745 !important;
    }
    .text-dark {
        color: #343a40 !important;
    }
    .text-center {
        text-align: center !important;
    }
    .text-right {
        text-align: right !important;
    }
    *, ::before, ::after {
        box-sizing: border-box;
        margin: 0;
    }
    .btn:not(:disabled):not(.disabled) {
        cursor: pointer;
    }
    .btn {
        display: inline-block;
        font-weight: 400;
        color: #212529;
        text-align: center;
        vertical-align: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        background-color: transparent;
        border: 1px solid transparent;
            border-top-color: transparent;
            border-right-color: transparent;
            border-bottom-color: transparent;
            border-left-color: transparent;
        padding: 0.375rem 0.75rem;
        font-size: 1rem;
        line-height: 1.5;
        border-radius: 0.25rem;
        transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    }
    .btn-success {
        color: #fff;
        background-color: #28a745;
        border-color: #28a745;
    }
    a {
        color: #007bff;
        text-decoration: none;
        background-color: transparent;
    }
    .mr-2, .mx-2 {
        margin-right: 0.5rem !important;
    }
    .btn-outline-success {
        color: #28a745;
        border-color: #28a745;
    }
    .mb-4, .my-4 {
        margin-bottom: 1.5rem !important;
    }
    .mt-4, .my-4 {
        margin-top: 1.5rem !important;
    }
    hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
        border: 0;
            border-top-color: currentcolor;
            border-top-style: none;
            border-top-width: 0px;
        border-top: 1px solid rgba(0, 0, 0, 0.1);
    }
    hr {
        box-sizing: content-box;
        height: 0;
        overflow: visible;
    }
    .left {
      float: left;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="p-4 col">
        <h1 class="text-success">WEBOTHOD.RU</h1>
        <hr class="my-4">
        <h2>{{ title }}</h2>
        <div class="card mt-3 mb-3">
          <div class="card-body">
            <p class="card-text">
              <h4>Заявка успешно создана и отправлена на модерацию.</h4>
              Ваш логин: {{ email }}<br />
              Пароль: {{ password }}<br />
              <a href="https://webothod.ru/user/signin" target="_self">Авторизоваться</a>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="row m-1">
      <div class="col-md-4 p-4 bg-light left">
        <a href="tel:+79221942202" class="text-success">+7 (922) 194-22-02</a>
      </div>
      <div class="col-md-4 p-4 bg-light text-dark text-center left">
        &copy; 2020 webothod.ru
      </div>
      <div class="col-md-4 p-4 bg-light text-right left">
        <a href="mailto:info@webothod.ru" class="text-success">info@webothod.ru</a>
      </div>
    </div>
  </div>
</body>
</html>