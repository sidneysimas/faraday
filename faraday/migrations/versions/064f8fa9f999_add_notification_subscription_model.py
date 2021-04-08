"""add_notification_subscription_model

Revision ID: 064f8fa9f999
Revises: 077b7c925ded
Create Date: 2021-04-05 20:11:13.105977+00:00

"""
from alembic import op
import sqlalchemy as sa
from faraday.server.fields import JSONType
from depot.fields.sqlalchemy import UploadedFileField


# revision identifiers, used by Alembic.
revision = '064f8fa9f999'
down_revision = '6471033046cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification_subscription',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.Enum('new_workspace', 'new_agent', 'new_user', 'new_agent_scan', 'new_report_scan', 'new_vulnerability', name='notification_events'), nullable=True),
    sa.Column('global_subscription', sa.Boolean(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['faraday_user.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['update_user_id'], ['faraday_user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('notification_subscription_base_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('type', sa.String(length=24), nullable=True),
    sa.ForeignKeyConstraint(['subscription_id'], ['notification_subscription.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_subscription_base_config_subscription_id'), 'notification_subscription_base_config', ['subscription_id'], unique=False)

    op.create_table('notification_subscription_mail_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('user_notified_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['notification_subscription_base_config.id'], ),
    sa.ForeignKeyConstraint(['user_notified_id'], ['faraday_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_subscription_mail_config_user_notified_id'), 'notification_subscription_mail_config', ['user_notified_id'], unique=False)

    op.create_table('notification_subscription_webhook_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['notification_subscription_base_config.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('notification_subscription_websocket_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_notified_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['notification_subscription_base_config.id'], ),
    sa.ForeignKeyConstraint(['user_notified_id'], ['faraday_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_subscription_websocket_config_user_notified_id'), 'notification_subscription_websocket_config', ['user_notified_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_notification_subscription_websocket_config_user_notified_id'), table_name='notification_subscription_websocket_config')
    op.drop_table('notification_subscription_websocket_config')
    op.drop_table('notification_subscription_webhook_config')
    op.drop_index(op.f('ix_notification_subscription_mail_config_user_notified_id'), table_name='notification_subscription_mail_config')
    op.drop_table('notification_subscription_mail_config')
    op.drop_index(op.f('ix_notification_subscription_base_config_subscription_id'), table_name='notification_subscription_base_config')
    op.drop_table('notification_subscription_base_config')
    op.drop_table('notification_subscription')
    # Added a mano
    op.execute('DROP TYPE notification_events')

    # ### end Alembic commands ###
