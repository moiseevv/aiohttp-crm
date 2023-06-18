
from app.store.crm.accessor import CrmAccessor

def setup_accessor(app):
    app.crm_accessor = CrmAccessor()
    app.on_startup.append(app.crm_accessor.connect)
    app.on_cleanup.append(app.crm_accessor.disconnect)