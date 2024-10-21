function validarRUT(rut) {
    const rutRegex = /^\d{1,2}\.?(\d{3}\.)\d{3}-[\dKk]$/;  // Permite con o sin puntos y guion
    if (!rutRegex.test(rut)) {
        return "El RUT no es válido. Formato correcto: XX.XXX.XXX-X o XX.XXXXXXX-X";
    }

    return null;
}

function validarNombreApellido(nombre) {
    const nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$/;
    if (!nombreRegex.test(nombre)) {
        return "El nombre o apellido contiene caracteres inválidos.";
    }
    if (nombre.length < 2) {
        return "El nombre o apellido es demasiado corto.";
    }
    return null;
}

function validarDireccion(direccion) {
    if (direccion.length < 5) {
        return "La dirección es demasiado corta.";
    }
    return null;
}

function validarTelefono(telefono) {
    const telefonoRegex = /^9?\d{8}$/;  // Ahora acepta un teléfono con o sin el prefijo 9
    if (!telefonoRegex.test(telefono)) {
        return "El teléfono no es válido. Debe tener 8 o 9 dígitos.";
    }
    return null;
}

function validarComuna(comuna) {
    if (comuna.length < 3) {
        return "El nombre de la comuna es demasiado corto.";
    }
    return null;
}

function validarFechaSolicitud(fecha) {
    const fechaActual = new Date();
    const fechaSolicitud = new Date(fecha);
    if (fechaSolicitud > fechaActual) {
        return "La fecha de solicitud no puede ser en el futuro.";
    }
    return null;
}

function validarFechaAceptacion(fechaSolicitud, fechaAceptacion) {
    const fechaSol = new Date(fechaSolicitud);
    const fechaAce = new Date(fechaAceptacion);
    if (fechaAce < fechaSol) {
        return "La fecha de aceptación no puede ser anterior a la fecha de solicitud.";
    }
    return null;
}

function validarEstado(estado) {
    const estadosValidos = ['PENDIENTE', 'ACEPTADA', 'RECHAZADA', 'EXPIRADA'];
    if (!estadosValidos.includes(estado)) {
        return "El estado no es válido. Debe ser uno de los siguientes: PENDIENTE, ACEPTADA, RECHAZADA, EXPIRADA.";
    }
    return null;
}

function validarFormulario(datos) {
    const { rut, nombre, apellido, direccion, telefono, comuna, fechaSolicitud, fechaAceptacion, estado } = datos;
    
    let errores = [];
    
    const errorRUT = validarRUT(rut);
    if (errorRUT) errores.push(errorRUT);
    
    const errorNombre = validarNombreApellido(nombre);
    if (errorNombre) errores.push(errorNombre);
    
    const errorApellido = validarNombreApellido(apellido);
    if (errorApellido) errores.push(errorApellido);
    
    const errorDireccion = validarDireccion(direccion);
    if (errorDireccion) errores.push(errorDireccion);
    
    const errorTelefono = validarTelefono(telefono);
    if (errorTelefono) errores.push(errorTelefono);
    
    const errorComuna = validarComuna(comuna);
    if (errorComuna) errores.push(errorComuna);
    
    const errorFechaSolicitud = validarFechaSolicitud(fechaSolicitud);
    if (errorFechaSolicitud) errores.push(errorFechaSolicitud);
    
    const errorFechaAceptacion = validarFechaAceptacion(fechaSolicitud, fechaAceptacion);
    if (errorFechaAceptacion) errores.push(errorFechaAceptacion);
    
    const errorEstado = validarEstado(estado);
    if (errorEstado) errores.push(errorEstado);

    return errores;
}

export { 
    validarFormulario, 
    validarRUT, 
    validarNombreApellido, 
    validarDireccion, 
    validarTelefono, 
    validarComuna, 
    validarFechaSolicitud, 
    validarFechaAceptacion, 
    validarEstado 
};
