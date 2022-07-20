

# Rascunho

## Variáveis base
v_0 = v_ini = volume inicial

CA = variação de 1 m3 no reservatório
CT = custo de 1 MWatt da termo

t_max = maximo que a hidreletrica pode fazer por mês

d_i = demanda da cidade

1m3 do reservatorio => kMWatt

i = mês

## Variáveis para resolver

p_t_i = producao da termo em um mês i
p_h_i = producao da hidro em um mês i

v_i = volume em um mes i
v_i_1 = volume em um mes i-1

dv_i = diferença de volume de i para i-1

w_p_i = "quantidade de água" usado para a produção em um mêsi

c_t_i = custo de produção da termo em um mês
c_h_i = custo de produção da hidro em um mês

p_i = producao total em um mês i

## Variáveis criadas por limitações do simplex
https://stackoverflow.com/a/28933583
dv_Pi = 
dv_Ni = 

# Restrições high-level
objetivo: minimizar o custo
- min ∑(ci)

- Todas devem ser maior ou igual que 0
    - `p_t_i, p_h_i, v_i, c_t_i, c_h_i, p_i ≥ 0`
- Produção total é da termo + hidro
    - `p_i = p_t_i + p_h_i`
- Custo da termo é a produção vezes o CT
    - `c_t_i = p_t_i * CT`
- Custo da hidro é a diferença de volume
    - `c_h_i = |dv_i| * CA`
- Diferença de volume é volume de um mês menos do outro
    - `dv_i = v_i - v_i_1`
- Produção da hidro em um mês deve ser menor que o máximo
    - `p_h_i < t_max`
- Volume em um mês i nunca deve ser maior que o máximo
    - `v_i ≤ v_max`
- Volume em um mês i nunca deve ser menor que o mínimo
    - `v_i ≥ v_min`
- Volume do mês i é o volume do mês anterior + a afluência do mês atual - a quantidade de água usada para a produção
    - `v_i = v_i_1 + y_1 - w_p_i`
- Água usada para a produção da hidro em um mês i deve ser, no máximo, o volume resultante do mês anterior + a afluência do mês atual
    - `w_p_i ≤ v_i_1 + y_1`
- Produção da hidro em um mês i é a água usada vezes a constante
    - `p_h_i = w_p_i * k`
- Produção de um mês i deve atender a demanda
    - `p_i ≥ d_i`
- Custo do mês i é igual a soma dos custos
    - `c_i = c_t_i + c_h_i`
- v_0 é o volume inicial
    - `v_0 = v_ini`
