@extends('layouts.app')
@section('content')


<div class="container">
    <div class="card">
        Informacion de Factura: {{$facturaKey}}
        <a href="{{ route('home')}}">Regresar</a>
        <br>
        <div id="attributesTable" >
			<table class="table table-dark">
                <tr>
                	<th scope="col">ID Producto</th>
                	<th scope="col">Valor</th>
                    <th scope="col">Valor con Tax</th>
               	</tr>
                @foreach ($detalles as $detalle)
                <tr>
                    <td>{{$detalle->producto_id}}</td>
                    <td>{{$detalle->precio }}</td>
                    <td>{{$detalle->total_con_tax }}</td>
                </tr>
                @endforeach
			</table>
        </div>
    </div>

</div>


@stop