from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from models.user import User
from persistence.mappings.mapping import Mapping


class UserMapping(Mapping):
    def create_table(self, metadata: MetaData) -> None:
        return Table(
            "user",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("email", String),
            Column("phone_number", String)
        )

    entity = User
