from services.line_parser import LineParser
from services.layouts import registry
from pathlib import Path
from services.load_json import AccountsManager

class PolizaFilter:
    def __init__(self, path):
        self.output_rows = []  # Store CSV rows
        self.parser = LineParser(registry) 
        self.file_path = path
    
    def clear(self) -> None:
        """Clear all stored rows"""
        # Reset the controller
        self.output_rows.clear() 

    def _process_header(self, header_data):
        """Process a header line into CA format"""
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
        return head_row

    def _process_movement(self, movement_data, num):
        """Process a movement line into CU format"""
        body_row = ['CU', num]
        for field in movement_data['layout'].fields:
            body_row.append(
                movement_data.get(field.name, 
                '0' if field.field_type in ('int', 'float') else '')
            )
        
        account = AccountsManager.get_account(movement_data.get('cuenta', ''))
        if account:
            body_row.append(account['main'])
            body_row.append(account['aux'])
        else:
            body_row.extend(['NA', 'NA'])
        return body_row
    
    def find(self, field, reference_list):
        """Find polizas matching the given field values"""
        self.clear()
        references = set(reference_list)  # Convert to set for O(1) lookups
        found_references = set()
        temp_buffer = []
        current_header_data = None
        current_movement_num = 0

        # Process each line in the file
        for parsed_line in self.parser.read_lines(str(self.file_path)):
            if not parsed_line.clean_line:
                continue

            try:
                if parsed_line.clean_line.startswith('P '):
                    # Save any existing buffer before processing new header
                    if temp_buffer:
                        self.output_rows.extend(temp_buffer)
                        temp_buffer = []
                    
                    # Process new header
                    header_data = parsed_line.layout.parse_line(parsed_line.clean_line)
                    header_value = header_data.get(field)

                    # Check if this is a header we want
                    if header_value in references and header_value not in found_references:
                        current_header_data = header_data
                        current_movement_num = 0
                        temp_buffer = [self._process_header(header_data)]
                        found_references.add(header_value)
                    else:
                        current_header_data = None
                        temp_buffer = []
                        current_movement_num = 0

                elif current_header_data and parsed_line.clean_line.startswith('M1'):
                    # Add movement to current buffer
                    current_movement_num += 1
                    movement_data = parsed_line.layout.parse_line(parsed_line.clean_line)
                    movement_data['layout'] = parsed_line.layout
                    temp_buffer.append(self._process_movement(movement_data, current_movement_num))

            except Exception as e:
                print(f"Error parsing line: {e}")
                continue

        # Add the last buffer if we have one
        if temp_buffer:
            self.output_rows.extend(temp_buffer)

        # Return True if we found all references, False otherwise
        return len(found_references) == len(references)