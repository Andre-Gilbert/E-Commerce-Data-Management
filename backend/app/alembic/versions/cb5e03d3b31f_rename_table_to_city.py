"""rename table to city

Revision ID: cb5e03d3b31f
Revises: 1f7007f42136
Create Date: 2022-04-14 14:27:07.206989

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cb5e03d3b31f'
down_revision = '1f7007f42136'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city', sa.Column('postal_code', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=True), sa.PrimaryKeyConstraint('postal_code'))
    op.create_index(op.f('ix_city_city'), 'city', ['city'], unique=False)
    op.create_index(op.f('ix_city_postal_code'), 'city', ['postal_code'], unique=False)
    op.drop_index('ix_postal_code_2_city_city', table_name='postal_code_2_city')
    op.drop_index('ix_postal_code_2_city_postal_code', table_name='postal_code_2_city')
    op.drop_table('postal_code_2_city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('postal_code_2_city', sa.Column('postal_code', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('postal_code', name='postal_code_2_city_pkey'))
    op.create_index('ix_postal_code_2_city_postal_code', 'postal_code_2_city', ['postal_code'], unique=False)
    op.create_index('ix_postal_code_2_city_city', 'postal_code_2_city', ['city'], unique=False)
    op.drop_index(op.f('ix_city_postal_code'), table_name='city')
    op.drop_index(op.f('ix_city_city'), table_name='city')
    op.drop_table('city')
    # ### end Alembic commands ###
