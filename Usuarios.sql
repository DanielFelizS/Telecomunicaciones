USE [master]
GO

/****** Object:  Database [Usuarios]    Script Date: 7/6/2023 9:09:17 a. m. ******/
CREATE DATABASE [Usuarios]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Usuarios', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\Usuarios.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Usuarios_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\Usuarios_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Usuarios].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [Usuarios] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [Usuarios] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [Usuarios] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [Usuarios] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [Usuarios] SET ARITHABORT OFF 
GO

ALTER DATABASE [Usuarios] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [Usuarios] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [Usuarios] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [Usuarios] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [Usuarios] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [Usuarios] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [Usuarios] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [Usuarios] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [Usuarios] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [Usuarios] SET  ENABLE_BROKER 
GO

ALTER DATABASE [Usuarios] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [Usuarios] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [Usuarios] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [Usuarios] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [Usuarios] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [Usuarios] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [Usuarios] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [Usuarios] SET RECOVERY FULL 
GO

ALTER DATABASE [Usuarios] SET  MULTI_USER 
GO

ALTER DATABASE [Usuarios] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [Usuarios] SET DB_CHAINING OFF 
GO

ALTER DATABASE [Usuarios] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [Usuarios] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [Usuarios] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [Usuarios] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO

ALTER DATABASE [Usuarios] SET QUERY_STORE = OFF
GO

ALTER DATABASE [Usuarios] SET  READ_WRITE 
GO

