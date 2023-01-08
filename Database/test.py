import sqlalchemy

# Connect to the database
engine = sqlalchemy.create_engine("postgresql://user:password@host:port/database")

# Create a bounding box object
class BoundingBox(object):
    def __init__(self, xmin, ymin, xmax, ymax, probability, image_name):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.probability = probability
        self.image_name = image_name

# Create a function to send the bounding box to the database
def send_to_database(box):
    # Create a connection to the database
    connection = engine.connect()

    # Create a new bounding box in the database
    connection.execute(
        "INSERT INTO bounding_boxes (xmin, ymin, xmax, ymax, probability, image_name) VALUES (:xmin, :ymin, :xmax, :ymax, :probability, :image_name)",
        xmin=box.xmin,
        ymin=box.ymin,
        xmax=box.xmax,
        ymax=box.ymax,
        probability=box.probability,
        image_name=box.image_name,
    )

    # Close the connection
    connection.close()

# Create a bounding box
box = BoundingBox(0, 0, 10, 10, 0.9, "image1.jpg")

# Send the bounding box to the database
send_to_database(box)