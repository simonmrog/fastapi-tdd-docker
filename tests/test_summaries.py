import json
import pytest


def test_read_all_summaries(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "new"})
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(
        list(filter(lambda d: d["id"] == summary_id, response_list))
    ) == 1


def test_read_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "test_string"})
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "test_string"
    assert response_dict["summary"] is not None
    assert response_dict["created_at"] is not None


def test_read_summary_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/summaries/000/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "string"})
    )


def test_create_summaries_invalid_json(test_app):
    response = test_app.post("/summaries/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
