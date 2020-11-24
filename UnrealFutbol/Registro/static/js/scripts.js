
            $(document).ready(function(){
            
                $("#registro").validate({
                    rules: {
                          email: {
                            required: true,
                            email: true
                          },
                          password: {
                              required: true,
                              minlength: 6,
  
                          },
                          password2: {
                              required: true,
                              
                              equalTo: "#password"
                              
    
                          },
                          
                          telefono: {
                              required: true,
                              minlength: 11,
                              number: true,
                              
                          },
                          nombre: "required",
                          fechaNacimiento: "required",
                          apellido: "required",
                                            
                      },
                      
                      messages: {
                          email: {
                              required: 'Ingresa tu correo electronico',
                              email: 'Formato de correo no valido',
                              
                          },
                          telefono: {
                              required: 'Ingresa un numero de celular',
                              minlength: 'Caracteres Insuficiente',
                              number: 'Caracter Invalido',
                          },
                          password2: {
                               required: 'Rengresa la contraseña',
                               equalTo: 'Las contraseñas ingresadas no coinciden',
                               minlength: 'Caracteres insuficiente'
    
                          },

                          nombre: {
                              required: 'Ingrese su Nombre',
                              
                          },

                          apellido: {
                              required: 'Ingrese su apellido',
                          },

                          fechaNacimiento: {
                              required: 'Ingrese fecha aceptada',
                          },

                          password: {
                              minlength: 'minimo 6 caracteres'

                          },
                      }
    
                  });

                  $("#login").validate({

                    rules: {
                        email: {
                            required: true,
                            email: true
                          },
                        
                          password: {
                            required: true,
                            minlength: 6,
                          },
                        
                    },

                    messages: {
                        email: {
                            required: 'Ingresa tu correo electronico',
                            email: 'Formato de correo no valido',
                            
                        },

                        password: {
                            required: 'Ingresa tu contraseña correctamente',

                        },

                    }

                  })

                  
                  
            
            });
            
    
        