from ast import parse
from pathlib import Path
from typing import Dict, Any
from services.line_parser import LineParser
from services.layouts import registry

class CSVPolizaController:
    def __init__(self):
        self.output_rows = []  # Store CSV rows
        self.parser = LineParser(registry)  # Same parser as JSON controller

    def parse_file(self, file_path: str | Path) -> None:
        """Parse a file and store rows in CSV format"""
        # Similar to JSON controller but format as CSV rows
        self.clear()

        # Track current header data for linking movements
        current_header_data = None
        current_movement_num = 0

        for parsed_line in self.parser.read_lines(str(file_path)):
            # Skip empty lines
            if not parsed_line.clean_line:
                continue

            if parsed_line.clean_line.startswith('P '):
                try:
                    header_data = parsed_line.layout.parse_line(parsed_line.clean_line)

                    current_movement_num = 0

                    head_row = ['CA']
                    head_row.extend([
                        header_data.get('fecha', ''),
                        header_data.get('tipo_pol', ''),
                        header_data.get('folio', ''),
                        header_data.get('clase', ''),
                        header_data.get('id_diario', ''),
                        header_data.get('concepto', ''),
                        header_data.get('sist_orig', ''),
                        header_data.get('impresa', '0'),
                        header_data.get('ajuste', '0'),
                        header_data.get('guid', '')
                    ])

                     # Add the header row
                    self.output_rows.append(head_row)

                    # Save header data for linking movements
                    current_header_data = header_data

                except Exception as e:
                    # Handle error - maybe add error row or log
                    print(f"Error parsing header: {e}")
            
            # If we have a header and this is a movement (M1)
            elif current_header_data and parsed_line.clean_line.startswith('M1'):
                try:
                    movement_data = parsed_line.layout.parse_line(parsed_line.clean_line)

                    current_movement_num +=1

                    # Format and store the CU row
                    body_row = ['CU']  # Start with identifier
                    # Get fields from layout dynamically
                    body_row.append(current_movement_num)
                    for field in parsed_line.layout.fields:
                        body_row.append(movement_data.get(field.name, '0' if field.field_type in ('int', 'float') else ''))

                    self.output_rows.append(body_row)

                except Exception as e:
                    # Handle error
                    print(f"Error parsing movement: {e}")
                     



    def write_csv(self, file_path: str | Path) -> None:
        """Write stored rows to a CSV file"""
        # Write self.output_rows to CSV
        import csv

        with open(file_path, 'w', newline='') as csv_f:
            writer = csv.writer(csv_f)
            writer.writerows(self.output_rows)

    def clear(self) -> None:
        """Clear all stored rows"""
        # Reset the controller
        self.output_rows.clear() 

    def format_header_row(self, header_data: dict) -> list:
        """Format a poliza header into a CA row"""
        # Convert header data to CSV format

    def format_movement_row(self, movement_data: dict) -> list:
        """Format a movement into a CU row"""
        # Convert movement data to CSV format