from django.shortcuts import render  
from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# --- VISTA PÚBLICA: Landing Page ZenithVet ---  
def bienvenida(request):  
    context = {  
        'titulo': 'ZenithVet',  
        'subtitulo': 'Sistema Integral de Gestión para Clínicas Veterinarias',  
        'mensaje': 'Gestiona tu clínica con inteligencia. Conecta con los dueños como nunca antes.',  
        'caracteristicas': [  
            {'icono': 'fa-calendar-check', 'titulo': 'Agenda Inteligente', 'descripcion': 'Gestión de citas sin doble booking con recordatorios automáticos'},  
            {'icono': 'fa-notes-medical', 'titulo': 'Historia Clínica Digital', 'descripcion': 'Expedientes completos con trazabilidad y adjuntos'},  
            {'icono': 'fa-boxes', 'titulo': 'Inventario + Retail', 'descripcion': 'Control de medicamentos, caducidades y productos de venta'},  
            {'icono': 'fa-cut', 'titulo': 'Módulo de Peluquería', 'descripcion': 'Agenda específica, precios por raza y servicios estéticos'},  
            {'icono': 'fa-calculator', 'titulo': 'Contabilidad y Nómina', 'descripcion': 'Facturación electrónica, gastos y control de empleados'},  
            {'icono': 'fa-building', 'titulo': 'Multi-Clínica', 'descripcion': 'Operación centralizada con métricas por sucursal'},  
            {'icono': 'fa-mobile-alt', 'titulo': 'App para Dueños', 'descripcion': 'Agenda, recordatorios y comunicación directa'},  
            {'icono': 'fa-chart-line', 'titulo': 'Reportes Analytics', 'descripcion': 'Dashboard con KPIs, ingresos y rendimiento'},  
        ],  
        'modulos': [  
            {  
                'nombre': 'Gestión Clínica',  
                'color': 'blue',  
                'items': ['Agenda', 'Historia Clínica', 'Recetas', 'Hospitalización']  
            },  
            {  
                'nombre': 'Inventario',  
                'color': 'green',  
                'items': ['Medicamentos', 'Productos Retail', 'Proveedores', 'Alertas de Stock']  
            },  
            {  
                'nombre': 'Financiero',  
                'color': 'purple',  
                'items': ['Caja Diaria', 'Facturación', 'Gastos', 'Nómina']  
            },  
            {  
                'nombre': 'Clientes',  
                'color': 'orange',  
                'items': ['Ficha de Mascotas', 'Historial', 'Recordatorios', 'App Móvil']  
            },  
        ],  
        'equipo': [  
            {'nombre': 'Dr. Sistema ZenithVet', 'rol': 'Plataforma SaaS', 'foto': 'https://placehold.co/150x150/2563eb/ffffff?text=ZV'},  
        ],  
    }  
    return render(request, 'bienvenida.html', context)  


# --- VISTA PROTEGIDA: Dashboard Principal (requiere login) ---  
@login_required  
def dashboard(request):  
    context = {  
        'titulo': 'Dashboard - ZenithVet',  
        'clinic_name': 'Mi Clínica Veterinaria',  
    }  
    return render(request, 'dashboard.html', context)  


# --- VISTA PROTEGIDA: Agenda ---  
@login_required  
def agenda(request):  
    context = {  
        'titulo': 'Agenda de Citas',  
    }  
    return render(request, 'agenda.html', context)  


# --- VISTA PROTEGIDA: Pacientes ---  
@login_required  
def pacientes(request):  
    context = {  
        'titulo': 'pacientes',  
    }  
    return render(request, 'pacientes.html', context) 

# --- VISTA PROTEGIDA: Inventario ---
@login_required
def inventario(request):
    context = {
        'titulo': 'Inventario',
    }
    return render(request, 'inventario.html', context)


# --- VISTA PROTEGIDA: Peluquería ---
@login_required
def peluqueria(request):
    context = {
        'titulo': 'Peluquería',
    }
    return render(request, 'peluqueria.html', context)


# --- VISTA PROTEGIDA: Caja Diaria ---
@login_required
def caja(request):
    context = {
        'titulo': 'Caja Diaria',
    }
    return render(request, 'caja.html', context)


# --- VISTA PROTEGIDA: Facturación ---
@login_required
def facturacion(request):
    context = {
        'titulo': 'Facturación',
    }
    return render(request, 'facturacion.html', context)


# --- VISTA PROTEGIDA: Clientes ---
@login_required
def clientes(request):
    context = {
        'titulo': 'Clientes',
    }
    return render(request, 'clientes.html', context)


# --- VISTA PROTEGIDA: Reportes ---
@login_required
def reportes(request):
    context = {
        'titulo': 'Reportes y Analytics',
    }
    return render(request, 'reportes.html', context)


def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form, 'titulo': 'Registro de Clínica'})

@login_required
def inventario(request):
    return render(request, 'dashboard.html', {'titulo': 'Inventario'})