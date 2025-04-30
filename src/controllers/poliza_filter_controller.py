from pathlib import Path
import csv
from .poliza_filter_csv import PolizaFilter

class PolizaFilterController:
    def __init__(self, input_path: str):
        """Initialize controller with input file path"""
        self.input_path = Path(input_path)
        self.filter = PolizaFilter(self.input_path)
    
    def filter_and_save(self, field: str, references: list, output_path: str) -> bool:
        """
        Filter polizas by field values and save results to CSV
        
        Args:
            field: Field name to filter by (e.g., 'folio', 'fecha')
            references: List of values to match against the field
            output_path: Path where to save the filtered results
        
        Returns:
            bool: True if all references were found, False otherwise
        """
        # Find matching polizas
        success = self.filter.find(field, references)
        
        # Save results to CSV
        if self.filter.output_rows:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.filter.output_rows)
        
        return success

    def get_results(self) -> list:
        """Get the filtered rows without saving to file"""
        return self.filter.output_rows
