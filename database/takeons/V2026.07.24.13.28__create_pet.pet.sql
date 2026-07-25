
CREATE TABLE pet.pet (
	name VARCHAR(100) NOT NULL, 
	image VARCHAR NOT NULL, 
	species species NOT NULL, 
	description VARCHAR NOT NULL, 
	status status NOT NULL, 
	id SERIAL NOT NULL, 
	created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

