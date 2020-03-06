
def writeCords(file,df,frame_no,frame_no_pos=1):
  atoms=df.shape[0]
  file.write(str(atoms)+'\n')
  if frame_no_pos==1:
    file.write('frame {} XYZ file generated by PYTHON code : coordinates in Angstrom\n'.format(frame_no))
  elif frame_no_pos==2:
    file.write('000 frame {} XYZ file generated by PYTHON code : coordinates in Angstrom\n'.format(frame_no))
  else:
    print('Invalid frame_no_pos {}'.format(frame_no_pos))
  for i in range(atoms):
    row=df.iloc[i,:]
    line=row['atom']+'  '+ \
        str(row['x'])+'  '+ \
        str(row['y'])+'  '+ \
        str(row['z'])+'\n'
    file.write(line)
  