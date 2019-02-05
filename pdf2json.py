
import tabula
import pandas as pd
import json
import io
#lel = tabula.read_pdf("Biophysics.pdf", java_options="-Dsun.java2d.cmm=sun.java2d.cmm.kcms.KcmsServiceProvider -Dfile.encoding=UTF-8", spreadsheet=False) #, stream=False) 
out = tabula.convert_into("Biophysics.pdf", "tmp.json", output_format="json", java_options="-Dsun.java2d.cmm=sun.java2d.cmm.kcms.KcmsServiceProvider")#,  -Dfile.encoding=UTF-16 spreadsheet=True, stream=False)
js_data = pd.read_json('tmp.json')['data'][0] 


ans = []
lowest_index = -228
last_q, last_a = "", ""

for q, a in js_data:

    q_up, a_up = q['top'], a['top']
    q_down, a_down = q_up + q['height'], a_up + a['height']

    cur_min = a_up
    if a_up == 0 or a_up < q_up:
        cur_min = q_up

    if cur_min > lowest_index + 9:
        ans.append({'q' : last_q, 'a': last_a})
        last_q, last_a = '', ''

    lowest_index = max([lowest_index, q_down, a_down])
    last_a += a['text']
    last_q += q['text']
    #print('q = {}, a = {}'.format(q['text'], a['text']), encoding='utf-8')


ans.append({'q' : last_q, 'a': last_a})
ans = ans[2:]


with open('data.json', 'w', encoding='utf-16') as outfile:
    json.dump(ans, outfile, indent = 4, ensure_ascii=False)
        
# with io.open('data.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(js_data, indent = 4, ensure_ascii=False))

# with open("out", "w") as f:
#     for line in out:
#         f.write(line)

# import pdfx
# pdf = pdfx.PDFx("Biophysics.pdf")
# metadata = pdf.get_metadata()
# reference_list = pdf.get_references()
# reference_dict = pdf.get_references_as_dict()
# print(metadata)
# print(reference_list)
# print(reference_dict)
#print(pdf.get_text())
#pdf.download_pdfs("target-directory")

