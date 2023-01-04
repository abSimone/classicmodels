from fastapi import FastAPI

import router.order as order
import router.customer as customer
import router.employee as employee
import router.payments as payments
import router.product as product
import router.productLines as productLines
import router.order_details as order_details
import router.office as office

app = FastAPI()

app.include_router(customer.router)
app.include_router(payments.router)
app.include_router(order.router)
app.include_router(order_details.router)
app.include_router(product.router)
app.include_router(productLines.router)
app.include_router(employee.router)
app.include_router(office.router)
