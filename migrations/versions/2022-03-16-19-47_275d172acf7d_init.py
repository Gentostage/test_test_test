"""init

Revision ID: 275d172acf7d
Revises: 
Create Date: 2022-03-16 19:47:40.822712

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '275d172acf7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, comment='Идентификатор'),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(timezone=True), nullable=False, comment='Дата рождения'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_patients'))
    )
    op.create_table('diagnoses',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, comment='Идентификатор'),
    sa.Column('patient_id', postgresql.UUID(as_uuid=True), nullable=False, comment='Идентификатор '),
    sa.Column('status', sa.String(), nullable=True, comment='Диагнозы'),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name=op.f('fk_diagnoses_patient_id_patients'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_diagnoses'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('diagnoses')
    op.drop_table('patients')
    # ### end Alembic commands ###
