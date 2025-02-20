class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    reward_points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Quest {self.name}>'
