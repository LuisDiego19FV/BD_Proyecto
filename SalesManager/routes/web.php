<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/home', 'HomeController@index')->name('home');
Route::post('/insertCliente', 'HomeController@insertCliente');
Route::post('/insertProduct', 'HomeController@insertProduct');

Route::get('/home/{productKey}', 'HomeController@productAttributes')->name('productAttributes');
Route::post('/insertAttribute', 'HomeController@insertAttribute');