@extends('layouts.app')
@section('content')


<div class="container">
    <div class="card">
        Informacion de Producto: {{$productKey}}
        <a href="{{ route('home')}}">Regresar</a>
        <form class ="my-form bg-dark"method="post" action="/insertAttribute">
            <label class="control-label text-light">Ingresar nuevo Atributo</label>
            <br>
            <label class="control-label text-light" for="atributo">Nombre</label>
            <input type="text" name="atributo" placeholder="Nombre">
            <br>

            <label class="control-label text-light" for="valor">Valor</label>
            <input type="text" name="valor" placeholder="Valor">
            <br>
            <input type="hidden" name="prodID" value="{{ $productKey }}">
            <input type="hidden" name="_token" value="{{ csrf_token() }}">
            <input type="submit" name="Sumbit">
        </form>
        <br>
        <div id="attributesTable" >
			<table class="table table-dark">
                <tr>
                	<th scope="col">Atributo</th>
                	<th scope="col">Valor</th>
               	</tr>
                @foreach ($attributes as $atributo)
                <tr>
                    <td>{{$atributo->atributo}}</td>
                    <td>{{$atributo->valor }}</td>
                </tr>
                @endforeach
			</table>
        </div>
    </div>

</div>


@stop