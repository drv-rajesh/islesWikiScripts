local p = {}

function p.parse(frame)
  local nexp = ""

  local unallowedc1 = "{"
  local unallowedc2 = "}"
  local unallowedc3 = "'"
  

  for char in frame.args[1]:gmatch"." do
    if unallowedc1 ~= char and unallowedc2 ~= char and unallowedc3 ~= char then
      nexp = nexp .. char
    end
  end

  return nexp
end

return p
