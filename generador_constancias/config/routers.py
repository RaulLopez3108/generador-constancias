class MyRouter:
    
    route_app_labels = {'constancias'} 

    def db_for_read(self, model, **hints):
        """Lee los modelos de 'constancias' desde 'base_datos'."""
        if model._meta.app_label in self.route_app_labels:
            return 'base_datos'
        return None

    def db_for_write(self, model, **hints):
        """Escribe los modelos de 'constancias' a 'base_datos'."""
        if model._meta.app_label in self.route_app_labels:
            return 'base_datos' # <-- CORRECCIÓN
        return None
    
    # allow_relation es trivial si no hay FKs entre bases de datos, pero se mantiene 
    # la lógica básica de separación.
    def allow_relation(self, obj1, obj2, **hints):
        # Permite relaciones internas a la app 'constancias'
        if obj1._meta.app_label in self.route_app_labels and \
           obj2._meta.app_label in self.route_app_labels:
            return True
        # Deja que Django decida para el resto de apps (usarán 'default')
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Asegura que los modelos de 'constancias' solo migren a 'base_datos'."""
        if app_label in self.route_app_labels:
            return db == 'base_datos'
        # Bloquea migraciones de cualquier otra cosa hacia 'base_datos'
        elif db == 'base_datos':
            return False
        return None