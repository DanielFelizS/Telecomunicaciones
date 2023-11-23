create database Telecomunicaciones
use Telecomunicaciones
go
-- Empleados --
create table Empleados(
Id int primary key identity,
Nombre varchar(15) not null,
Apellido varchar(40) not null,
Sexo char(1) not null,
Cargo varchar(25) not null,
Sueldo money not null,
Teléfono varchar(35) not null,
Dirección varchar(30),
Cédula Nvarchar(20) not null, 
FechaNacimiento varchar(20) not null,
Correo varchar(20),
Fecha_contratación varchar(20) not null,
Nacionalidad varchar(30) not null
);
go
alter table Empleados add constraint CK_Empleados_Sexo check (Sexo in('M', 'F'))
alter table Empleados add constraint UQ_Empleados_Correo unique (Correo)
alter table Empleados add constraint UQ_Empleados_Teléfono unique (Teléfono)
alter table Empleados add constraint UQ_Empleados_Cédula unique (Cédula)
alter table Empleados add constraint DF_Empleados_Sueldo default 0.00 for Sueldo
go
create proc Insert_empleados
@Nombre varchar(15),
@Apellido varchar(40),
@Sexo char(1),
@Cargo varchar(25),
@Sueldo money,
@Teléfono varchar(35),
@Dirección varchar(30),
@Cédula Nvarchar(20),
@FechaNacimiento varchar(20),
@Correo varchar(30),
@Fecha_contratación varchar(20),
@Nacionalidad varchar(30)
as
insert into Empleados(Nombre, Apellido, Sexo, Cargo, Sueldo, Teléfono, Dirección, Cédula, FechaNacimiento, Correo, Fecha_contratación, Nacionalidad)
values(@Nombre, @Apellido, @Sexo, @Cargo, @Sueldo, @Teléfono, @Dirección, @Cédula, @FechaNacimiento, @Correo, @Fecha_contratación, @Nacionalidad)
go
create proc Eliminar_empleado
@Cédula Nvarchar(20)
as
delete from Empleados where Cédula = @Cédula 
go
create proc Actualizar_empleados
@Nombre varchar(15),
@Apellido varchar(40),
@Sexo char(1),
@Cargo varchar(25),
@Sueldo money,
@Teléfono varchar(35),
@Dirección varchar(30),
@Cédula Nvarchar(20),
@FechaNacimiento varchar(20),
@Correo varchar(30),
@Fecha_contratación varchar(20),
@Nacionalidad varchar(30)
as
update Empleados set Nombre = @Nombre, Apellido = @Apellido, Sexo = @Sexo, Cargo = @Cargo, Sueldo = @Sueldo, Teléfono = @Teléfono,
Dirección = @Dirección, Cédula = @Cédula, FechaNacimiento = @FechaNacimiento, Correo = @Correo, Fecha_contratación = @Fecha_contratación, 
Nacionalidad = @Nacionalidad  where Cédula = @Cédula
go
select * from Empleados


go
exec Insert_empleados 'Eli', 'Munoz Pilar', 'M', 'Desarrollador Front-end', 50000, '809-1111-222', 'C.Keily #4',
'000-00000-2', '31/2/23', 'EliMunoz@gmail.com', '21/5/30', 'Dominicano'
go
truncate table Empleados
go
-- Clientes --
create table Clientes(
Id int identity(1,1) primary key,
Nombre varchar(15) not null,
Apellido varchar(40) not null,
Sexo char(1) not null,
Fecha_nacimiento Varchar(15) not null,
Direccion varchar(50) not null,
Sector varchar(40) not null,
Municipio varchar(45) not null,
Provincia varchar(45) not null,
Cédula Nvarchar(20) not null,
Correo Nvarchar(30) not null,
Teléfono Nvarchar(35) not null
);
go
alter table Clientes add constraint CK_Clientes_Sexo check (Sexo in('M', 'F'))
alter table Clientes add constraint UQ_Clientes_Cédula unique (Cédula)
alter table Clientes add constraint UQ_Clientes_Correo unique (Correo)
alter table Clientes add constraint UQ_Clientes_Teléfono unique (Teléfono)
go
create proc Insertar_clientes
@Nombre varchar(15),
@Apellido varchar(40),
@Sexo char(1),
@Fecha_nacimiento varchar(15),
@Direccion varchar(50),
@Sector varchar(40),
@Municipio varchar(45),
@Provincia varchar(45),
@Cédula Nvarchar(20),
@Correo varchar(30),
@Teléfono varchar(35)
as
insert into Clientes(Nombre, Apellido, Sexo, Fecha_nacimiento, Direccion, Sector, Municipio, Provincia, Cédula, Correo, Teléfono)
values(@Nombre, @Apellido, @Sexo, @Fecha_nacimiento, @Direccion, @Sector, @Municipio, @Provincia, @Cédula, @Correo, @Teléfono)
go
exec Insertar_clientes 'Daniel', 'Feliz Santana', 'M', '12/5/23', 'C.18 #62 Luis M. Caraballo 3ro',
'Sabana Perdida', 'Santo Domingo Norte', 'Santo Domingo', '402-1213236-5', 'felizd223@gmail.com', '849-446-9260' 
select * from Clientes
go
create proc Eliminar_cliente
@Cédula Nvarchar(20)
as
delete from Clientes where Cédula = @Cédula 
go
create proc Actualizar_cliente
@Id int,
@Nombre varchar(15),
@Apellido varchar(40),
@Sexo char(1),
@Fecha_nacimiento date,
@Direccion varchar(50),
@Sector varchar(40),
@Municipio varchar(45),
@Provincia varchar(45),
@Cédula Nvarchar(20),
@Correo varchar(30),
@Teléfono varchar(35)
as
update Clientes set Nombre = @Nombre, Apellido = @Apellido, Sexo = @Sexo, Fecha_nacimiento = @Fecha_nacimiento, Direccion = @Direccion,
Sector = @Sector, Municipio = @Municipio, Provincia = @Provincia, Cédula = @Cédula, Correo = @Correo, Teléfono = @Teléfono where Id = @Id
go
-- Servicios --
create table Servicios(
Id int identity(1,1) primary key,
Nombre_cliente varchar(15) not null,
Nombre_empleado varchar(15) not null,
Nombre_equipo varchar(15) not null,
Nombre_servicio varchar(30) not null,
Descripcion varchar(50) not null,
Precio money not null,
Tipo_plan varchar(30) not null 
);
go
select * from Servicios
exec Insertar_Servicios  'Daniel', 'Eli', 'Antena', 'Empresa', 'Antena Claro', 6000, 'Cable/Satélite'
go
alter table Servicios add constraint CK_Servicios_Tipo_plan check (Tipo_plan in ('Móvil', 'Teléfono residencial', 'Cable/Satélite', 'Internet'))
alter table Servicios add constraint Fk_Servicios_Nombre_cliente foreign key (Id) references Clientes(Id)
alter table Servicios add constraint Fk_Servicios_Nombre_empleado foreign key (Id) references Empleados(Id)
alter table Servicios add constraint Fk_Servicios_Nombre_equipo foreign key (Id) references Equipos(Id)
go
create proc Insertar_Servicios
@Nombre_cliente varchar(15),
@Nombre_empleado varchar(15),
@Nombre_equipo varchar(15),
@Nombre_servicio varchar(30),
@Descripcion varchar(50),
@Precio money,
@Tipo_plan varchar(30)
as
insert into Servicios(Nombre_cliente, Nombre_empleado, Nombre_equipo, Nombre_servicio, Descripcion, Precio, Tipo_plan)values
(@Nombre_cliente, @Nombre_empleado, @Nombre_equipo, @Nombre_servicio, @Descripcion, @Precio, @Tipo_plan)
go
create proc Eliminar_Servicio
@Nombre_cliente varchar(15)
as
delete from Servicios where Nombre_cliente = @Nombre_cliente
go
create proc Actualizar_Servicio
@Id int,
@Nombre_cliente varchar(15),
@Nombre_empleado varchar(15),
@Nombre_equipo varchar(15),
@Nombre_servicio varchar(30),
@Descripcion varchar(50),
@Precio money,
@Tipo_plan varchar(30)
as
update Servicios set Nombre_cliente = @Nombre_cliente, Nombre_empleado = @Nombre_empleado, Nombre_equipo = @Nombre_equipo, 
Descripcion = @Descripcion, Precio = @Precio, Tipo_plan = @Tipo_plan where Id = @Id
go
-- Equipos --
create table Equipos(
Id int primary key identity(1,1),
tipo varchar(25) not null,
fecha_fabricación varchar(25) not null
);
go
alter table Equipos add constraint CK_Equipos_Tipo check (tipo in ('Antena', 'Router', 'Teléfono', 'Celular'))
go
select * from Equipos
go
create proc Insertar_Equipos
@tipo varchar(25),
@fecha_fabricación varchar(25)
as
insert into Equipos(tipo, fecha_fabricación)values(@tipo, @fecha_fabricación)
go
create proc Eliminar_Equipo
@fecha_fabricación varchar(25)
as
delete from Equipos where fecha_fabricación = @fecha_fabricación
go
create proc Actualizar_Equipo
@tipo varchar(25),
@fecha_fabricación varchar(25)
as
update Equipos set tipo = @tipo, fecha_fabricación = @fecha_fabricación where fecha_fabricación = @fecha_fabricación
-- Facturas --
create table Facturación(
id int primary key identity(1,1),
Nombre_cliente varchar(15) not null,
Nombre_empleado varchar(15) not null,
Nombre_servicio varchar(30) not null,
Nombre_equipo varchar(30) not null,
fecha varchar(25) not null,
descripcion varchar(30) not null
);
go
alter table Facturación add constraint CK_Facturación_Nombre_equipo check (Nombre_equipo in ('Antena', 'Router', 'Teléfono', 'Celular'))
alter table Facturación add constraint FK_Facturación_Nombre_cliente foreign key (Id) references Clientes(Id)
alter table Facturación add constraint FK_Facturación_Nombre_empleado foreign key (Id) references Empleados(Id)
alter table Facturación add constraint FK_Facturación_Nombre_servicio foreign key (Id) references Servicios(Id)
alter table Facturación add constraint FK_Facturación_Nombre_equipo foreign key (Id) references Equipos(Id)
go
select * from Facturación
exec Insert_Factura 'Keily', 'Eli', 'Internet', 'Router', '2/3/23', 'Keily el mejor'
go
create proc Insert_Factura
@Nombre_cliente varchar(15),
@Nombre_empleado varchar(15),
@Nombre_servicio varchar(30),
@Nombre_equipo varchar(30),
@fecha varchar(25),
@descripcion varchar(30)
as
insert into Facturación(Nombre_cliente, Nombre_empleado, Nombre_servicio, Nombre_equipo, fecha, descripcion)
values(@Nombre_cliente, @Nombre_empleado, @Nombre_servicio, @Nombre_equipo, @fecha, @descripcion)
go
create proc Eiminar_Factura
@Nombre_cliente varchar(15)
as
delete from Facturación where Nombre_cliente = @Nombre_cliente
go
create proc Actualizar_Factura
@Nombre_cliente varchar(15),
@Nombre_empleado varchar(15),
@Nombre_servicio varchar(30),
@Nombre_equipo varchar(30),
@fecha varchar(25),
@descripcion varchar(30)
as
update Facturación set Nombre_cliente = @Nombre_cliente, Nombre_empleado = @Nombre_empleado, Nombre_servicio = @Nombre_servicio,
Nombre_equipo = @Nombre_equipo, fecha = @fecha, descripcion = @descripcion 
where fecha = @fecha
go

select E.Nombre as 'Nombre_empleado', C.Nombre as 'Nombre_cliente', C.Sexo as 'Sexo_cliente', 
S.Nombre_servicio as 'Servicio', EQ.tipo as 'Tipo_equipo', F.fecha as 'Fecha_facturación' from Empleados as E 
join Facturación as F on F.Id = F.Id join Servicios as S on S.Id = S.Id join Clientes as C on C.Id =  S.Id 
join Equipos as EQ on EQ.Id =  S.Id

select * from Empleados
