@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))
    
    else:
        # re-present form for Editing
        return render_template("pet_add_form.html", form=form")

    @app.route("/<int:pet_id>", methods=["GET", "POST"])
    def edit_pet(pet_id):
        # Edit pet
    
        pet = Pet.query.get_or_404(pet_id)
        form = EditPetForm(obj=pet)

        if form.validate_on_submit():
            pet.notes = form.notes.data
            pet.available = form.available.data
            pet.photo_url = form.photo_url.data
            db.session.commit()
            flash(f"{pet.name} updated.")
            return redirect(url_for('list_pets'))

        else:
            # failed; re-present form for editing pet
            return render_template("pet_edit_form.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", method=['GET'])
def api_get_pet(pet_id):
    # """return basic info about pet in JSON"""     

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)