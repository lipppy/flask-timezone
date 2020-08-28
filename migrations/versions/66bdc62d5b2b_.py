"""empty message

Revision ID: 66bdc62d5b2b
Revises: 17b231f28690
Create Date: 2020-08-15 15:51:38.222357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66bdc62d5b2b'
down_revision = '17b231f28690'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('published', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('spatial_ref_sys')
    op.drop_index('all_tz_geom_idx', table_name='timezones_utc')
    op.drop_table('timezones_utc')
    op.drop_index('dateline_geom_idx', table_name='dateline')
    op.drop_table('dateline')
    op.drop_index('timezones_world_mp_geom_idx', table_name='timezones_world')
    op.drop_table('timezones_world')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timezones_world',
    sa.Column('gid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('tzid', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type=u'MULTIPOLYGON', from_text='ST_GeomFromEWKT', name='geometry'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('gid', name=u'timezones_world_mp_pkey')
    )
    op.create_index('timezones_world_mp_geom_idx', 'timezones_world', ['geom'], unique=False)
    op.create_table('dateline',
    sa.Column('gid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('scalerank', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('name_long', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('abbrev', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('note', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('featurecla', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type=u'MULTILINESTRING', from_text='ST_GeomFromEWKT', name='geometry'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('gid', name=u'dateline_pkey')
    )
    op.create_index('dateline_geom_idx', 'dateline', ['geom'], unique=False)
    op.create_table('timezones_utc',
    sa.Column('gid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type=u'MULTIPOLYGON', from_text='ST_GeomFromEWKT', name='geometry'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('gid', name=u'all_tz_pkey')
    )
    op.create_index('all_tz_geom_idx', 'timezones_utc', ['geom'], unique=False)
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint(u'(srid > 0) AND (srid <= 998999)', name=u'spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name=u'spatial_ref_sys_pkey')
    )
    op.drop_table('books')
    # ### end Alembic commands ###
