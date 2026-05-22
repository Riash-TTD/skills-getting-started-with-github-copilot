def test_get_activities_returns_seeded_activity_data(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in body
    assert {"description", "schedule", "max_participants", "participants"}.issubset(
        body[expected_activity].keys()
    )
