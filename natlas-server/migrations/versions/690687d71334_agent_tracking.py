"""agent tracking

Revision ID: 690687d71334
Revises: e59d726ef9c1
Create Date: 2019-04-10 13:22:50.238639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690687d71334'
down_revision = 'e59d726ef9c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('agentid', sa.String(length=16), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('friendly_name', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_agent_agentid'), 'agent', ['agentid'], unique=True)
    op.create_index(op.f('ix_agent_token'), 'agent', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_agent_token'), table_name='agent')
    op.drop_index(op.f('ix_agent_agentid'), table_name='agent')
    op.drop_table('agent')
    # ### end Alembic commands ###
