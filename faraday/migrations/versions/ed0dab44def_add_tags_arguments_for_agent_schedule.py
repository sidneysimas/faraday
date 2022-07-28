"""add_tags_arguments_for_agent_schedule

Revision ID: 0ed0dab44def
Revises: f82a9136c408
Create Date: 2022-07-19 13:31:17.646914+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed0dab44def'
down_revision = '99a740945c44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agent_schedule', sa.Column('vuln_tag', sa.String(), nullable=True))
    op.add_column('agent_schedule', sa.Column('service_tag', sa.String(), nullable=True))
    op.add_column('agent_schedule', sa.Column('host_tag', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('agent_schedule', 'host_tag')
    op.drop_column('agent_schedule', 'service_tag')
    op.drop_column('agent_schedule', 'vuln_tag')
    # ### end Alembic commands ###
