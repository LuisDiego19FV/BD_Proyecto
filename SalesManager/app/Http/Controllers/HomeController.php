<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Form;
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
        $marcas = DB::table('public.marcas')->get();
        $categorias = DB::table('public.categorias')->get();
        return view('home')->with('origin', $clientes)->with('products', $productos)->with('facturas', $facturas)->with('marcas', $marcas)->with('categorias', $categorias);
        
        
    }
    public function insertCliente(request $request ){
        DB::table('public.clientes')->insert([ 'nit' => $request->nit, 'primer_nombre' => $request->primer_nombre, 'apellido' =>$request->apellido]); 
        return back();
    }

    public function insertProduct(request $request ){
        DB::select('SELECT add_product(?,?)', array($request->marca, $request->categoria));
        return back();
    }

    public function productAttributes(request $request){
        $attributes = DB::table('public.productos')->where('id', '=', $request->productKey)->get();
        return view('productAttributes')->with('attributes', $attributes)->with('productKey', $request->productKey);
    }

    public function insertAttribute(request $request){
        DB::table('public.productos')->insert(['id' => $request->prodID, 'atributo' => $request->atributo, 'valor' => $request->valor]);
        return back();



    }
}
