from app.models.prize import Prize
import json
import os

class PrizeDatabase:
    def __init__(self):
        data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

        prizes_json_path = os.path.join(data_directory, 'prizes.json')
        self.all_prizes = []

        with open(prizes_json_path) as f:
            all_prizes_json = json.load(f)

            for elem in all_prizes_json:
                self.all_prizes.append(
                    Prize(id=elem.get("id"), catalog_id=elem.get("catalog_id"), title=elem.get("title"), description=elem.get("description"), image=elem.get("image"))
                )

    def get_prizes(self, catalog_id, filter_params=None, pagination_params=None):
        filtered_prizes = self.all_prizes
        filtered_prizes = [prize for prize in filtered_prizes if prize.catalog_id == catalog_id]

        if filter_params and 'id' in filter_params:
            filtered_prizes = [prize for prize in filtered_prizes if prize.id == filter_params['id']]

        if filter_params and 'description' in filter_params:
            filtered_prizes = [prize for prize in filtered_prizes if filter_params['description'].lower() in prize.description.lower()]

        page = pagination_params.get('page', 1) if pagination_params else 1
        per_page = pagination_params.get('per_page', 10) if pagination_params else 10

        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_prizes = filtered_prizes[start_idx:end_idx]

        return {'total': len(filtered_prizes), 'prizes': [prize.to_dict() for prize in paginated_prizes]}
