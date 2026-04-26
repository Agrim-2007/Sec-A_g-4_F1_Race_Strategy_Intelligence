"""
Update all notebooks to filter data to 2010-2025 (exclude incomplete 2026)
"""
import json
import re

notebooks_to_update = [
    'notebooks/03_eda.ipynb',
    'notebooks/04_statistical_analysis.ipynb'
]

for notebook_path in notebooks_to_update:
    print(f"\n{'='*80}")
    print(f"Updating {notebook_path}")
    print('='*80)
    
    with open(notebook_path, 'r') as f:
        nb = json.load(f)
    
    changes_made = 0
    
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code' and 'source' in cell:
            source_text = ''.join(cell['source'])
            original_source = source_text
            
            # Pattern 1: Filter with only >= 2010
            if "master_fact['year'] >= 2010" in source_text and "master_fact['year'] <=" not in source_text:
                # Update to include upper bound
                source_text = source_text.replace(
                    "master_fact['year'] >= 2010",
                    "(master_fact['year'] >= 2010) &\n    (master_fact['year'] <= 2025)"
                )
                
                # Also update constructor_kpis if present
                if "constructor_kpis['year'] >= 2010" in source_text:
                    source_text = source_text.replace(
                        "constructor_kpis['year'] >= 2010",
                        "(constructor_kpis['year'] >= 2010) &\n    (constructor_kpis['year'] <= 2025)"
                    )
                
                if source_text != original_source:
                    cell['source'] = source_text.split('\n')
                    # Add newlines back
                    cell['source'] = [line + '\n' if i < len(cell['source'])-1 else line 
                                     for i, line in enumerate(cell['source'])]
                    cell['outputs'] = []
                    cell['execution_count'] = None
                    changes_made += 1
                    print(f"  ✅ Updated cell {i}: Added year <= 2025 filter")
        
        elif cell['cell_type'] == 'markdown' and 'source' in cell:
            source_text = ''.join(cell['source'])
            original_source = source_text
            
            # Update markdown text references
            source_text = source_text.replace('2010-2024', '2010-2025')
            source_text = source_text.replace('2010–2024', '2010–2025')
            source_text = re.sub(r'\(2010-2024\)', '(2010-2025)', source_text)
            
            if source_text != original_source:
                cell['source'] = source_text.split('\n')
                cell['source'] = [line + '\n' if i < len(cell['source'])-1 else line 
                                 for i, line in enumerate(cell['source'])]
                changes_made += 1
                print(f"  ✅ Updated cell {i}: Changed text 2010-2024 → 2010-2025")
    
    # Save updated notebook
    with open(notebook_path, 'w') as f:
        json.dump(nb, f, indent=1)
    
    print(f"\n  Total changes: {changes_made}")

print("\n" + "="*80)
print("✅ ALL NOTEBOOKS UPDATED TO 2010-2025")
print("="*80)
print("\nNext: Re-run notebooks 03 and 04 to regenerate outputs")
