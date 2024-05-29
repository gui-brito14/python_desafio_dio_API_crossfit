"""
Revision ID: ${up_revision}
Revises: ${down_revision | none}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa

<% if message %>
"""${message}"""
<% endif %>

# revision identifiers, used by Alembic.
revision = '${up_revision}'
down_revision = ${repr(down_revision) | none}
branch_labels = ${repr(branch_labels) | none}
depends_on = ${repr(depends_on) | none}

def upgrade():
    ${upgrades if upgrades else 'pass'}

def downgrade():
    ${downgrades if downgrades else 'pass'}
