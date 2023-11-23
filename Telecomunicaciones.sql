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
Tel�fono varchar(35) not null,
Direcci�n varchar(30),
C�dula Nvarchar(20) not null, 
FechaNacimiento varchar(20) not null,
Correo varchar(20),
Fecha_contrataci�n varchar(20) not null,
Nacionalidad varchar(30) not null
);
go
alter table Empleados add constraint CK_Empleados_Sexo check (Sexo in('M', 'F'))
alter table Empleados add constraint UQ_Empleados_Correo unique (Correo)
alter table Empleados add constraint UQ_Empleados_Tel�fono unique (Tel�fono)
alter table Empleados add constraint UQ_Empleados_C�dula unique (C�dula)
alter table Empleados add constraint DF_Empleados_Sueldo default 0.00 for Sueldo
go
create proc Insert_empleados
@Nombre varchar(15),
@Apellido varchar(40),
@Sexo char(1),
@Cargo varchar(25),
@Sueldo money,
@Tel�fono varchar(35),
@Direcci�n varchar(30),
@C�dula Nvarchar(20),
@FechaNacimiento varchar(20),
@Correo varchar(30),
@Fecha_contrataci�n varchar(20),
@Nacionalidad varchar(30)
as
insert into Empleados(Nombre, Apellido, Sexo, Cargo, Sueldo, Tel�fono, Direcci�n, C�dula, FechaNacimiento, Correo, Fecha_contrataci�n, Nacionalidad)
values(@Nombre, @Apellido, @Sexo, @Cargo, @Sueldo, @Tel�fono, @Direcci�n, @C�dula, @FechaNacimiento, @Correo, @Fecha_contrataci�n, @Nacionalidad)
go
create proc Eliminar_empleado
@C�dula Nvarchar(20)
as
delete from Empleados where C�dula = @C�dula 
go
create proc Actualizar_empleados
@Nombre varchar(15),
@Apellido varchar(40),
@Sexo char(1),
@Cargo varchar(25),
@Sueldo money,
@Tel�fono varchar(35),
@Direcci�n varchar(30),
@C�dula Nvarchar(20),
@FechaNacimiento varchar(20),
@Correo varchar(30),
@Fecha_contrataci�n varchar(20),
@Nacionalidad varchar(30)
as
update Empleados set Nombre = @Nombre, Apellido = @Apellido, Sexo = @Sexo, Cargo = @Cargo, Sueldo = @Sueldo, Tel�fono = @Tel�fono,
Direcci�n = @Direcci�n, C�dula = @C�dula, FechaNacimiento = @FechaNacimiento, Correo = @Correo, Fecha_contrataci�n = @Fecha_contrataci�n, 
Nacionalidad = @Nacionalidad  where C�dula = @C�dula
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
C�dula Nvarchar(20) not null,
Correo Nvarchar(30) not null,
Tel�fono Nvarchar(35) not null
);
go
alter table Clientes add constraint CK_Clientes_Sexo check (Sexo in('M', 'F'))
alter table Clientes add constraint UQ_Clientes_C�dula unique (C�dula)
alter table Clientes add constraint UQ_Clientes_Correo unique (Correo)
alter table Clientes add constraint UQ_Clientes_Tel�fono unique (Tel�fono)
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
@C�dula Nvarchar(20),
@Correo varchar(30),
@Tel�fono varchar(35)
as
insert into Clientes(Nombre, Apellido, Sexo, Fecha_nacimiento, Direccion, Sector, Municipio, Provincia, C�dula, Correo, Tel�fono)
values(@Nombre, @Apellido, @Sexo, @Fecha_nacimiento, @Direccion, @Sector, @Municipio, @Provincia, @C�dula, @Correo, @Tel�fono)
go
exec Insertar_clientes 'Daniel', 'Feliz Santana', 'M', '12/5/23', 'C.18 #62 Luis M. Caraballo 3ro',
'Sabana Perdida', 'Santo Domingo Norte', 'Santo Domingo', '402-1213236-5', 'felizd223@gmail.com', '849-446-9260' 
select * from Clientes
go
create proc Eliminar_cliente
@C�dula Nvarchar(20)
as
delete from Clientes where C�dula = @C�dula 
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
@C�dula Nvarchar(20),
@Correo varchar(30),
@Tel�fono varchar(35)
as
update Clientes set Nombre = @Nombre, Apellido = @Apellido, Sexo = @Sexo, Fecha_nacimiento = @Fecha_nacimiento, Direccion = @Direccion,
Sector = @Sector, Municipio = @Municipio, Provincia = @Provincia, C�dula = @C�dula, Correo = @Correo, Tel�fono = @Tel�fono where Id = @Id
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
exec Insertar_Servicios  'Daniel', 'Eli', 'Antena', 'Empresa', 'Antena Claro', 6000, 'Cable/Sat�lite'
go
alter table Servicios add constraint CK_Servicios_Tipo_plan check (Tipo_plan in ('M�vil', 'Tel�fono residencial', 'Cable/Sat�lite', 'Internet'))
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
fecha_fabricaci�n varchar(25) not null
);
go
alter table Equipos add constraint CK_Equipos_Tipo check (tipo in ('Antena', 'Router', 'Tel�fono', 'Celular'))
go
select * from Equipos
go
create proc Insertar_Equipos
@tipo varchar(25),
@fecha_fabricaci�n varchar(25)
as
insert into Equipos(tipo, fecha_fabricaci�n)values(@tipo, @fecha_fabricaci�n)
go
create proc Eliminar_Equipo
@fecha_fabricaci�n varchar(25)
as
delete from Equipos where fecha_fabricaci�n = @fecha_fabricaci�n
go
create proc Actualizar_Equipo
@tipo varchar(25),
@fecha_fabricaci�n varchar(25)
as
update Equipos set tipo = @tipo, fecha_fabricaci�n = @fecha_fabricaci�n where fecha_fabricaci�n = @fecha_fabricaci�n
-- Facturas --
create table Facturaci�n(
id int primary key identity(1,1),
Nombre_cliente varchar(15) not null,
Nombre_empleado varchar(15) not null,
Nombre_servicio varchar(30) not null,
Nombre_equipo varchar(30) not null,
fecha varchar(25) not null,
descripcion varchar(30) not null
);
go
alter table Facturaci�n add constraint CK_Facturaci�n_Nombre_equipo check (Nombre_equipo in ('Antena', 'Router', 'Tel�fono', 'Celular'))
alter table Facturaci�n add constraint FK_Facturaci�n_Nombre_cliente foreign key (Id) references Clientes(Id)
alter table Facturaci�n add constraint FK_Facturaci�n_Nombre_empleado foreign key (Id) references Empleados(Id)
alter table Facturaci�n add constraint FK_Facturaci�n_Nombre_servicio foreign key (Id) references Servicios(Id)
alter table Facturaci�n add constraint FK_Facturaci�n_Nombre_equipo foreign key (Id) references Equipos(Id)
go
select * from Facturaci�n
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
insert into Facturaci�n(Nombre_cliente, Nombre_empleado, Nombre_servicio, Nombre_equipo, fecha, descripcion)
values(@Nombre_cliente, @Nombre_empleado, @Nombre_servicio, @Nombre_equipo, @fecha, @descripcion)
go
create proc Eiminar_Factura
@Nombre_cliente varchar(15)
as
delete from Facturaci�n where Nombre_cliente = @Nombre_cliente
go
create proc Actualizar_Factura
@Nombre_cliente varchar(15),
@Nombre_empleado varchar(15),
@Nombre_servicio varchar(30),
@Nombre_equipo varchar(30),
@fecha varchar(25),
@descripcion varchar(30)
as
update Facturaci�n set Nombre_cliente = @Nombre_cliente, Nombre_empleado = @Nombre_empleado, Nombre_servicio = @Nombre_servicio,
Nombre_equipo = @Nombre_equipo, fecha = @fecha, descripcion = @descripcion 
where fecha = @fecha
go

select E.Nombre as 'Nombre_empleado', C.Nombre as 'Nombre_cliente', C.Sexo as 'Sexo_cliente', 
S.Nombre_servicio as 'Servicio', EQ.tipo as 'Tipo_equipo', F.fecha as 'Fecha_facturaci�n' from Empleados as E 
join Facturaci�n as F on F.Id = F.Id join Servicios as S on S.Id = S.Id join Clientes as C on C.Id =  S.Id 
join Equipos as EQ on EQ.Id =  S.Id

select * from Empleados
