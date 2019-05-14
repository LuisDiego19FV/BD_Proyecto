@extends('layouts.app')
@section('content')


<div class="container">

            <ul class="nav nav-pills">
                <li class="nav-item"><a class ="active nav-link" data-toggle="pill" href="#tableView">Ver Tablas</a></li>
                <li class="nav-item"><a class="nav-link" data-toggle="pill" href="#insertView">Insertar Informacion</a></li>
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
                                        <th scope="col">Eliminar</th>
                                   	</tr>
                                    @foreach ($origin as $originf)
                                    <tr>
                                        <td>{{$originf->nit}}</td>
                                        <td>{{$originf->primer_nombre }}</td>
                                        <td>{{$originf->apellido }}</td>
                                        <td>
                                            <button type="submit" name="Sumbit"><i class= "fas fa-user-minus "style="color: red;"></i></button>
                                        </td>
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
                                        
                                        <td><a href="{{ route('productAttributes', [$producto->productid]) }}" target="_blank">{{$producto->productid}}</td>
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
                                        <td><a href="{{ route('detalleFactura', [$factura->id]) }}" target="_blank">{{$factura->id}}</td>
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

                        <ul class="nav nav-pills flex-column">
                            <li class="nav-item"><a class="active nav-link" data-toggle="pill" href="#clientInsert">Agregar Cliente</a></li>
                            <li class="nav-item"><a class="nav-link" data-toggle="pill" href="#productosInsert">Agregar Producto</a></li>
                        </ul>

                        <div class="tab-content">

                            <div id="clientInsert" class="tab-pane fade-in active">
                				<form class ="my-form bg-dark"method="post" action="/insertCliente">
                                    <label class="control-label text-light" for="nit">NIT:</label>
                					<input type="text" name="nit" placeholder="NIT">
                                    <br>

                                    <label class="control-label text-light" for="primer_nombre">Primer Nombre:</label>
                					<input type="text" name="primer_nombre" placeholder="Primer Nombre">
                                    <br>

                                    <label class="control-label text-light" for="apellido">Apellido:</label>
                					<input type="text" name="apellido" placeholder="Apellidos">
                                    <br>

                					<input type="hidden" name="_token" value="{{ csrf_token() }}">
                					<input type="submit" name="Sumbit">
                				</form>
                            </div>

                            <div id="productosInsert" class="tab-pane fade">
                                <form class ="my-form bg-dark" method="post" action="/insertProduct">
                                    <label class="control-label text-light" for="marca">Marca:</label>
                                    <select name="marca" id="marca" class="form-control">
                                        @foreach($marcas as $marca)
                                        <option value="{{ $marca->id }}">{{ $marca->nombre }}</option>
                                        @endforeach
                                    </select>
                                    <br>

                                    <label class="control-label text-light" for="categoria">Categoria:</label>
                                    <select name="categoria" id="categoria" class="form-control">
                                        @foreach($categorias as $categoria)
                                        <option value="{{ $categoria->id }}">{{ $categoria->nombre }}</option>
                                        @endforeach
                                    </select>
                                    <br>

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