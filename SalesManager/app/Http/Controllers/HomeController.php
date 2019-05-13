<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\Redirect;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;


class HomeController extends Controller
{
        /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
            
        $clientes = DB::table('public.clientes')->get();
        $productos = DB::table('public.vw_productwithbrandandcategory')->get();
        $facturas = DB::table('public.vw_facturawithtotal')->get();

        return view('home')->with('origin', $clientes)->with('products', $productos)->with('facturas', $facturas);
        
        
    }
    public function insertCliente(request $request ){
        DB::table('public.clientes')->insert([ 'nit' => $request->nit, 'primer_nombre' => $request->primer_nombre, 'apellido' =>$request->apellido]); 
        return Redirect::to('home');
    }
}
