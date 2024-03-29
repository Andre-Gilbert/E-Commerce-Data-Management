"""create database

Revision ID: 471585ac9ad5
Revises: 2022-06-21 13:24:12.123456
Create Date: 2022-06-10 17:55:25.452818

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '471585ac9ad5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # user
    op.create_table('user', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('token_version', sa.Integer(), nullable=False), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)

    # city
    op.create_table('city', sa.Column('postal_code', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True), sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('postal_code'))
    op.create_index('city_postal_code_uc', 'city', ['postal_code', 'name'], unique=True)
    op.create_index(op.f('ix_city_name'), 'city', ['name'], unique=False)
    op.create_index(op.f('ix_city_edited_by'), 'city', ['edited_by'], unique=False)
    op.create_index(op.f('ix_city_postal_code'), 'city', ['postal_code'], unique=False)

    # address
    op.create_table('address', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False), sa.Column('region', sa.String(), nullable=True),
                    sa.Column('postal_code', sa.String(), nullable=True),
                    sa.Column('street', sa.String(), nullable=False),
                    sa.Column('house_number', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['postal_code'],
                        ['city.postal_code'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_address_country'), 'address', ['country'], unique=False)
    op.create_index(op.f('ix_address_edited_by'), 'address', ['edited_by'], unique=False)
    op.create_index(op.f('ix_address_house_number'), 'address', ['house_number'], unique=False)
    op.create_index(op.f('ix_address_id'), 'address', ['id'], unique=False)
    op.create_index(op.f('ix_address_postal_code'), 'address', ['postal_code'], unique=False)
    op.create_index(op.f('ix_address_region'), 'address', ['region'], unique=False)
    op.create_index(op.f('ix_address_street'), 'address', ['street'], unique=False)

    # warehouse
    op.create_table('warehouse', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('address_id', sa.Integer(), nullable=True), sa.Column('email',
                                                                                    sa.String(),
                                                                                    nullable=False),
                    sa.Column('phone_number', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['address_id'],
                        ['address.id'],
                    ), sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_warehouse_address_id'), 'warehouse', ['address_id'], unique=False)
    op.create_index(op.f('ix_warehouse_edited_by'), 'warehouse', ['edited_by'], unique=False)
    op.create_index(op.f('ix_warehouse_email'), 'warehouse', ['email'], unique=True)
    op.create_index(op.f('ix_warehouse_id'), 'warehouse', ['id'], unique=False)
    op.create_index(op.f('ix_warehouse_phone_number'), 'warehouse', ['phone_number'], unique=True)

    # department
    op.create_table('department', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False), sa.Column('manager_id', sa.Integer(),
                                                                              nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_department_edited_by'), 'department', ['edited_by'], unique=False)
    op.create_index(op.f('ix_department_id'), 'department', ['id'], unique=False)
    op.create_index(op.f('ix_department_manager_id'), 'department', ['manager_id'], unique=False)
    op.create_index(op.f('ix_department_name'), 'department', ['name'], unique=False)

    # employee
    op.create_table('employee', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('ssn', sa.String(), nullable=True), sa.Column('salutation', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('job_title', sa.String(), nullable=False),
                    sa.Column('department_id', sa.Integer(), nullable=True),
                    sa.Column('warehouse_id', sa.Integer(), nullable=True),
                    sa.Column('address_id', sa.Integer(), nullable=True), sa.Column('email',
                                                                                    sa.String(),
                                                                                    nullable=False),
                    sa.Column('phone_number', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['address_id'],
                        ['address.id'],
                    ), sa.ForeignKeyConstraint(
                        ['department_id'],
                        ['department.id'],
                    ), sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['warehouse_id'],
                        ['warehouse.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_employee_address_id'), 'employee', ['address_id'], unique=False)
    op.create_index(op.f('ix_employee_department_id'), 'employee', ['department_id'], unique=False)
    op.create_index(op.f('ix_employee_edited_by'), 'employee', ['edited_by'], unique=False)
    op.create_index(op.f('ix_employee_email'), 'employee', ['email'], unique=True)
    op.create_index(op.f('ix_employee_first_name'), 'employee', ['first_name'], unique=False)
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=False)
    op.create_index(op.f('ix_employee_job_title'), 'employee', ['job_title'], unique=False)
    op.create_index(op.f('ix_employee_last_name'), 'employee', ['last_name'], unique=False)
    op.create_index(op.f('ix_employee_phone_number'), 'employee', ['phone_number'], unique=True)
    op.create_index(op.f('ix_employee_salutation'), 'employee', ['salutation'], unique=False)
    op.create_index(op.f('ix_employee_ssn'), 'employee', ['ssn'], unique=True)
    op.create_index(op.f('ix_employee_warehouse_id'), 'employee', ['warehouse_id'], unique=False)

    op.create_foreign_key(
        'fk_department_manager_id',
        'department',
        'employee',
        ['manager_id'],
        ['id'],
    )

    # category
    op.create_table('category', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False), sa.Column('description', sa.String(),
                                                                              nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_category_description'), 'category', ['description'], unique=False)
    op.create_index(op.f('ix_category_edited_by'), 'category', ['edited_by'], unique=False)
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=True)

    # customer
    op.create_table('customer', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('salutation', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False), sa.Column('email', sa.String(),
                                                                                   nullable=False),
                    sa.Column('phone_number', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_customer_edited_by'), 'customer', ['edited_by'], unique=False)
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_index(op.f('ix_customer_first_name'), 'customer', ['first_name'], unique=False)
    op.create_index(op.f('ix_customer_id'), 'customer', ['id'], unique=False)
    op.create_index(op.f('ix_customer_last_name'), 'customer', ['last_name'], unique=False)
    op.create_index(op.f('ix_customer_phone_number'), 'customer', ['phone_number'], unique=True)
    op.create_index(op.f('ix_customer_salutation'), 'customer', ['salutation'], unique=False)

    # payment_information
    op.create_table('payment_information', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('iban', sa.String(), nullable=False), sa.Column('bic', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_payment_information_bic'), 'payment_information', ['bic'], unique=False)
    op.create_index(op.f('ix_payment_information_edited_by'), 'payment_information', ['edited_by'], unique=False)
    op.create_index(op.f('ix_payment_information_iban'), 'payment_information', ['iban'], unique=True)
    op.create_index(op.f('ix_payment_information_id'), 'payment_information', ['id'], unique=False)

    # payment_information_2_customer
    op.create_table('payment_information_2_customer', sa.Column('customer_id', sa.Integer(), nullable=False),
                    sa.Column('payment_information_id', sa.Integer(), nullable=False),
                    sa.Column('is_default', sa.Boolean(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['customer_id'],
                        ['customer.id'],
                    ), sa.ForeignKeyConstraint(
                        ['payment_information_id'],
                        ['payment_information.id'],
                    ), sa.PrimaryKeyConstraint('customer_id', 'payment_information_id'))
    op.create_index(op.f('ix_payment_information_2_customer_customer_id'),
                    'payment_information_2_customer', ['customer_id'],
                    unique=False)
    op.create_index(op.f('ix_payment_information_2_customer_edited_by'),
                    'payment_information_2_customer', ['edited_by'],
                    unique=False)
    op.create_index(op.f('ix_payment_information_2_customer_payment_information_id'),
                    'payment_information_2_customer', ['payment_information_id'],
                    unique=False)

    # address_2_customer
    op.create_table('address_2_customer', sa.Column('customer_id', sa.Integer(), nullable=False),
                    sa.Column('address_id', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['address_id'],
                        ['address.id'],
                    ), sa.ForeignKeyConstraint(
                        ['customer_id'],
                        ['customer.id'],
                    ), sa.PrimaryKeyConstraint('customer_id', 'address_id'))
    op.create_index(op.f('ix_address_2_customer_address_id'), 'address_2_customer', ['address_id'], unique=False)
    op.create_index(op.f('ix_address_2_customer_customer_id'), 'address_2_customer', ['customer_id'], unique=False)
    op.create_index(op.f('ix_address_2_customer_edited_by'), 'address_2_customer', ['edited_by'], unique=False)

    # shipping_service
    op.create_table('shipping_service', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False), sa.Column('address_id', sa.Integer(),
                                                                              nullable=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('phone_number', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['address_id'],
                        ['address.id'],
                    ), sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_shipping_service_address_id'), 'shipping_service', ['address_id'], unique=False)
    op.create_index(op.f('ix_shipping_service_edited_by'), 'shipping_service', ['edited_by'], unique=False)
    op.create_index(op.f('ix_shipping_service_email'), 'shipping_service', ['email'], unique=True)
    op.create_index(op.f('ix_shipping_service_id'), 'shipping_service', ['id'], unique=False)
    op.create_index(op.f('ix_shipping_service_name'), 'shipping_service', ['name'], unique=False)
    op.create_index(op.f('ix_shipping_service_phone_number'), 'shipping_service', ['phone_number'], unique=True)

    # supplier
    op.create_table('supplier', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False), sa.Column('address_id', sa.Integer(),
                                                                              nullable=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('phone_number', sa.String(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['address_id'],
                        ['address.id'],
                    ), sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_supplier_address_id'), 'supplier', ['address_id'], unique=False)
    op.create_index(op.f('ix_supplier_edited_by'), 'supplier', ['edited_by'], unique=False)
    op.create_index(op.f('ix_supplier_email'), 'supplier', ['email'], unique=True)
    op.create_index(op.f('ix_supplier_id'), 'supplier', ['id'], unique=False)
    op.create_index(op.f('ix_supplier_name'), 'supplier', ['name'], unique=False)
    op.create_index(op.f('ix_supplier_phone_number'), 'supplier', ['phone_number'], unique=True)

    # order
    op.create_table('order', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('customer_id', sa.Integer(), nullable=True),
                    sa.Column('status', sa.Enum('OPEN', 'SENT', 'DELIVERED', name='orderstatus'), nullable=False),
                    sa.Column('order_date', sa.Date(), nullable=False),
                    sa.Column('address_id', sa.Integer(), nullable=True),
                    sa.Column('employee_id', sa.Integer(), nullable=True),
                    sa.Column('shipping_service_id', sa.Integer(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['address_id'],
                        ['address.id'],
                    ), sa.ForeignKeyConstraint(
                        ['customer_id'],
                        ['customer.id'],
                    ), sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['employee_id'],
                        ['employee.id'],
                    ), sa.ForeignKeyConstraint(
                        ['shipping_service_id'],
                        ['shipping_service.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_order_address_id'), 'order', ['address_id'], unique=False)
    op.create_index(op.f('ix_order_customer_id'), 'order', ['customer_id'], unique=False)
    op.create_index(op.f('ix_order_edited_by'), 'order', ['edited_by'], unique=False)
    op.create_index(op.f('ix_order_employee_id'), 'order', ['employee_id'], unique=False)
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_index(op.f('ix_order_order_date'), 'order', ['order_date'], unique=False)
    op.create_index(op.f('ix_order_shipping_service_id'), 'order', ['shipping_service_id'], unique=False)
    op.create_index(op.f('ix_order_status'), 'order', ['status'], unique=False)

    # invoice
    op.create_table('invoice', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('status', sa.Enum('OPEN', 'OVERDUE', 'PAID', name='invoicestatus'), nullable=False),
                    sa.Column('issue_date', sa.Date(), nullable=False), sa.Column('due_date', sa.Date(),
                                                                                  nullable=False),
                    sa.Column('order_id', sa.Integer(), nullable=True),
                    sa.Column('payment_information_id', sa.Integer(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['order_id'],
                        ['order.id'],
                    ), sa.ForeignKeyConstraint(
                        ['payment_information_id'],
                        ['payment_information.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_invoice_due_date'), 'invoice', ['due_date'], unique=False)
    op.create_index(op.f('ix_invoice_edited_by'), 'invoice', ['edited_by'], unique=False)
    op.create_index(op.f('ix_invoice_id'), 'invoice', ['id'], unique=False)
    op.create_index(op.f('ix_invoice_issue_date'), 'invoice', ['issue_date'], unique=False)
    op.create_index(op.f('ix_invoice_order_id'), 'invoice', ['order_id'], unique=True)
    op.create_index(op.f('ix_invoice_payment_information_id'), 'invoice', ['payment_information_id'], unique=False)
    op.create_index(op.f('ix_invoice_status'), 'invoice', ['status'], unique=False)

    # product
    op.create_table('product', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False), sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('description', sa.String()), sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.Column('description', sa.String()), sa.Column('supplier_id', sa.Integer(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['category_id'],
                        ['category.id'],
                    ), sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['supplier_id'],
                        ['supplier.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_product_category_id'), 'product', ['category_id'], unique=False)
    op.create_index(op.f('ix_product_edited_by'), 'product', ['edited_by'], unique=False)
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=False)
    op.create_index(op.f('ix_product_price'), 'product', ['price'], unique=False)
    op.create_index(op.f('ix_product_supplier_id'), 'product', ['supplier_id'], unique=False)

    # order_2_product
    op.create_table('order_2_product', sa.Column('order_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('price_at_time_of_purchase', sa.Float(), nullable=False),
                    sa.Column('number_of_items', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['order_id'],
                        ['order.id'],
                    ), sa.ForeignKeyConstraint(
                        ['product_id'],
                        ['product.id'],
                    ), sa.PrimaryKeyConstraint('order_id', 'product_id'))
    op.create_index(op.f('ix_order_2_product_edited_by'), 'order_2_product', ['edited_by'], unique=False)
    op.create_index(op.f('ix_order_2_product_number_of_items'), 'order_2_product', ['number_of_items'], unique=False)
    op.create_index(op.f('ix_order_2_product_order_id'), 'order_2_product', ['order_id'], unique=False)
    op.create_index(op.f('ix_order_2_product_price_at_time_of_purchase'),
                    'order_2_product', ['price_at_time_of_purchase'],
                    unique=False)
    op.create_index(op.f('ix_order_2_product_product_id'), 'order_2_product', ['product_id'], unique=False)

    # product_2_warehouse
    op.create_table('product_2_warehouse', sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('warehouse_id', sa.Integer(), nullable=False),
                    sa.Column('number_in_stock', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('updated', sa.DateTime(), nullable=True),
                    sa.Column('edited_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['edited_by'],
                        ['user.id'],
                    ), sa.ForeignKeyConstraint(
                        ['product_id'],
                        ['product.id'],
                    ), sa.ForeignKeyConstraint(
                        ['warehouse_id'],
                        ['warehouse.id'],
                    ), sa.PrimaryKeyConstraint('product_id', 'warehouse_id'))
    op.create_index(op.f('ix_product_2_warehouse_edited_by'), 'product_2_warehouse', ['edited_by'], unique=False)
    op.create_index(op.f('ix_product_2_warehouse_number_in_stock'),
                    'product_2_warehouse', ['number_in_stock'],
                    unique=False)
    op.create_index(op.f('ix_product_2_warehouse_product_id'), 'product_2_warehouse', ['product_id'], unique=False)
    op.create_index(op.f('ix_product_2_warehouse_warehouse_id'), 'product_2_warehouse', ['warehouse_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_2_warehouse_warehouse_id'), table_name='product_2_warehouse')
    op.drop_index(op.f('ix_product_2_warehouse_product_id'), table_name='product_2_warehouse')
    op.drop_index(op.f('ix_product_2_warehouse_number_in_stock'), table_name='product_2_warehouse')
    op.drop_index(op.f('ix_product_2_warehouse_edited_by'), table_name='product_2_warehouse')
    op.drop_table('product_2_warehouse')
    op.drop_index(op.f('ix_order_2_product_product_id'), table_name='order_2_product')
    op.drop_index(op.f('ix_order_2_product_price_at_time_of_purchase'), table_name='order_2_product')
    op.drop_index(op.f('ix_order_2_product_order_id'), table_name='order_2_product')
    op.drop_index(op.f('ix_order_2_product_number_of_items'), table_name='order_2_product')
    op.drop_index(op.f('ix_order_2_product_edited_by'), table_name='order_2_product')
    op.drop_table('order_2_product')
    op.drop_index(op.f('ix_product_supplier_id'), table_name='product')
    op.drop_index(op.f('ix_product_price'), table_name='product')
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_index(op.f('ix_product_edited_by'), table_name='product')
    op.drop_index(op.f('ix_product_category_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_invoice_status'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_payment_information_id'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_order_id'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_issue_date'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_id'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_edited_by'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_due_date'), table_name='invoice')
    op.drop_table('invoice')
    op.drop_index(op.f('ix_order_status'), table_name='order')
    op.drop_index(op.f('ix_order_shipping_service_id'), table_name='order')
    op.drop_index(op.f('ix_order_order_date'), table_name='order')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_index(op.f('ix_order_employee_id'), table_name='order')
    op.drop_index(op.f('ix_order_edited_by'), table_name='order')
    op.drop_index(op.f('ix_order_customer_id'), table_name='order')
    op.drop_index(op.f('ix_order_address_id'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_supplier_phone_number'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_name'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_id'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_email'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_edited_by'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_address_id'), table_name='supplier')
    op.drop_table('supplier')
    op.drop_index(op.f('ix_shipping_service_phone_number'), table_name='shipping_service')
    op.drop_index(op.f('ix_shipping_service_name'), table_name='shipping_service')
    op.drop_index(op.f('ix_shipping_service_id'), table_name='shipping_service')
    op.drop_index(op.f('ix_shipping_service_email'), table_name='shipping_service')
    op.drop_index(op.f('ix_shipping_service_edited_by'), table_name='shipping_service')
    op.drop_index(op.f('ix_shipping_service_address_id'), table_name='shipping_service')
    op.drop_table('shipping_service')
    op.drop_index(op.f('ix_address_2_customer_edited_by'), 'address_2_customer')
    op.drop_index(op.f('ix_address_2_customer_customer_id'), 'address_2_customer')
    op.drop_index(op.f('ix_address_2_customer_address_id'), 'address_2_customer')
    op.drop_table('address_2_customer')
    op.drop_index(op.f('ix_payment_information_2_customer_payment_information_id'),
                  table_name='payment_information_2_customer')
    op.drop_index(op.f('ix_payment_information_2_customer_edited_by'), table_name='payment_information_2_customer')
    op.drop_index(op.f('ix_payment_information_2_customer_customer_id'), table_name='payment_information_2_customer')
    op.drop_table('payment_information_2_customer')
    op.drop_index(op.f('ix_payment_information_id'), table_name='payment_information')
    op.drop_index(op.f('ix_payment_information_iban'), table_name='payment_information')
    op.drop_index(op.f('ix_payment_information_edited_by'), table_name='payment_information')
    op.drop_index(op.f('ix_payment_information_bic'), table_name='payment_information')
    op.drop_table('payment_information')
    op.drop_index(op.f('ix_customer_salutation'), table_name='customer')
    op.drop_index(op.f('ix_customer_phone_number'), table_name='customer')
    op.drop_index(op.f('ix_customer_last_name'), table_name='customer')
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.drop_index(op.f('ix_customer_first_name'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_index(op.f('ix_customer_edited_by'), table_name='customer')
    op.drop_table('customer')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_index(op.f('ix_category_edited_by'), table_name='category')
    op.drop_index(op.f('ix_category_description'), table_name='category')
    op.drop_table('category')
    op.drop_constraint('fk_department_manager_id')
    op.drop_index(op.f('ix_employee_warehouse_id'), table_name='employee')
    op.drop_index(op.f('ix_employee_ssn'), table_name='employee')
    op.drop_index(op.f('ix_employee_salutation'), table_name='employee')
    op.drop_index(op.f('ix_employee_phone_number'), table_name='employee')
    op.drop_index(op.f('ix_employee_last_name'), table_name='employee')
    op.drop_index(op.f('ix_employee_job_title'), table_name='employee')
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    op.drop_index(op.f('ix_employee_first_name'), table_name='employee')
    op.drop_index(op.f('ix_employee_email'), table_name='employee')
    op.drop_index(op.f('ix_employee_edited_by'), table_name='employee')
    op.drop_index(op.f('ix_employee_department_id'), table_name='employee')
    op.drop_index(op.f('ix_employee_address_id'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_department_name'), table_name='department')
    op.drop_index(op.f('ix_department_manager_id'), table_name='department')
    op.drop_index(op.f('ix_department_id'), table_name='department')
    op.drop_index(op.f('ix_department_edited_by'), table_name='department')
    op.drop_table('department')
    op.drop_index(op.f('ix_warehouse_phone_number'), table_name='warehouse')
    op.drop_index(op.f('ix_warehouse_id'), table_name='warehouse')
    op.drop_index(op.f('ix_warehouse_email'), table_name='warehouse')
    op.drop_index(op.f('ix_warehouse_edited_by'), table_name='warehouse')
    op.drop_index(op.f('ix_warehouse_address_id'), table_name='warehouse')
    op.drop_table('warehouse')
    op.drop_index(op.f('ix_address_street'), table_name='address')
    op.drop_index(op.f('ix_address_region'), table_name='address')
    op.drop_index(op.f('ix_address_postal_code'), table_name='address')
    op.drop_index(op.f('ix_address_id'), table_name='address')
    op.drop_index(op.f('ix_address_house_number'), table_name='address')
    op.drop_index(op.f('ix_address_edited_by'), table_name='address')
    op.drop_index(op.f('ix_address_country'), table_name='address')
    op.drop_table('address')
    op.drop_index(op.f('ix_city_postal_code'), table_name='city')
    op.drop_index(op.f('ix_city_edited_by'), table_name='city')
    op.drop_index(op.f('ix_city_city'), table_name='city')
    op.drop_index('city_postal_code_uc', table_name='city')
    op.drop_table('city')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
