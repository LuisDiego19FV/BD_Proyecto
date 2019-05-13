@extends('layouts.app')
@section('content')


<div class="container">

    <div class ="container-column">

        <div class="col-md-8">
            <ul class="nav nav-pills">
                <li class="nav-item"><a class ="active nav-link" data-toggle="pill" href="#tableView">Table View</a></li>
                <li class="nav-item"><a class="nav-link" data-toggle="pill" href="#insertView">Insert</a></li>
            </ul>

            <div class="card">

                <div class="tab-content">
                   
                    <div id="tableView" class="tab-pane fade-in active">
                        <ul class="nav nav-pills flex-column">
                            <li class="nav-item"><a class="active nav-link" data-toggle="pill" href="#clientTable">Ver Clientes</a></li>
                            <li class="nav-item"><a class="nav-link" data-toggle="pill" href="#productosTable">Ver Productos</a></li>
                            <li class="nav-item"><a class="nav-link" data-toggle="pill" href="#facturasTable">Ver Facturas</a></li>
                        </ul>
                        <div class="tab-content">
                            <div id="clientTable" class="tab-pane fade-in active">
                				<table class="table table-dark">
                                    <tr>
                                    	<th scope="col">NIT</th>
                                    	<th scope="col">Primer Nombre</th>
                                    	<th scope="col">Apellido</th>
                                   	</tr>
                                    @foreach ($origin as $originf)
                                    <tr>
                                        <td>{{$originf->nit}}</td>
                                        <td>{{$originf->primer_nombre }}</td>
                                        <td>{{$originf->apellido }}</td>
                                    </tr>
                                    @endforeach
                				</table>
                            </div>
                            <div id="productosTable" class="tab-pane fade">
                                <table class="table table-dark">
                                    <tr>
                                        <th scope="col">Product ID</th>
                                        <th scope="col">Marca</th>
                                        <th scope="col">Categoria</th>
                                    </tr>
                                    @foreach ($products as $producto)
                                    <tr>
                                        <td>{{$producto->productid}}</td>
                                        <td>{{$producto->marca }}</td>
                                        <td>{{$producto->categoria }}</td>
                                    </tr>
                                    @endforeach
                                </table>
                            </div>
                            <div id="facturasTable" class="tab-pane fade">
                                <table class="table table-dark">
                                    <tr>
                                        <th scope="col">No. Factura</th>
                                        <th scope="col">NIT</th>
                                        <th scope="col">Lugar</th>
                                        <th scope="col">Hora</th>
                                        <th scope="col">Total</th>
                                    </tr>
                                    @foreach ($facturas as $factura)
                                    <tr>
                                        <td>{{$factura->id}}</td>
                                        <td>{{$factura->nit }}</td>
                                        <td>{{$factura->lugar }}</td>
                                        <td>{{$factura->tiempo }}</td>
                                        <td>{{$factura->total }}</td>
                                    </tr>
                                    @endforeach
                                </table>
                            </div>
                        </div>
                    </div>

                    <div id="insertView" class="tab-pane fade">
        				<form method="post" action="/insertCliente">
        					<input type="text" name="nit" placeholder="NIT">
        					<input type="text" name="primer_nombre" placeholder="primer_nombre">
        					<input type="text" name="apellido" placeholder="apellido">
        					<input type="hidden" name="_token" value="{{ csrf_token() }}">
        					<input type="submit" name="Sumbit">
        				</form>
                    </div>

				</div>

            </div>
        </div>
    </div>
</div>



@stop