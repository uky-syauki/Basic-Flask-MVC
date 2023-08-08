"""First Update

Revision ID: f0dc95fdda5a
Revises: 
Create Date: 2023-07-23 08:05:51.858441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0dc95fdda5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama', sa.String(length=25), nullable=True),
    sa.Column('password', sa.String(length=25), nullable=True),
    sa.Column('email', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('barang',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('kode_barang', sa.String(length=10), nullable=True),
    sa.Column('nama_barang', sa.String(length=25), nullable=True),
    sa.Column('harga_modal', sa.Integer(), nullable=True),
    sa.Column('harga_jual', sa.Integer(), nullable=True),
    sa.Column('stok', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('barang', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_barang_kode_barang'), ['kode_barang'], unique=True)

    op.create_table('recorduang',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ket', sa.String(length=10), nullable=True),
    sa.Column('nilai', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    with op.batch_alter_table('recorduang', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_recorduang_timestamp'), ['timestamp'], unique=False)

    op.create_table('transaksi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('kode_barang', sa.String(length=10), nullable=True),
    sa.Column('harga_jual', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.ForeignKeyConstraint(['kode_barang'], ['barang.kode_barang'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('transaksi', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_transaksi_id'), ['id'], unique=True)
        batch_op.create_index(batch_op.f('ix_transaksi_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaksi', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_transaksi_timestamp'))
        batch_op.drop_index(batch_op.f('ix_transaksi_id'))

    op.drop_table('transaksi')
    with op.batch_alter_table('recorduang', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recorduang_timestamp'))

    op.drop_table('recorduang')
    with op.batch_alter_table('barang', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_barang_kode_barang'))

    op.drop_table('barang')
    op.drop_table('admin')
    # ### end Alembic commands ###
