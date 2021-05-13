store = {}
store['timestamp']=1620296205
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=13']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=13
store['worker_id']=13
store['num_workers']=40
store['config']={'seed': 16, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1374473571777344})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.434230327606201})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.629298210144043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7301888465881348})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6957, 'crossentropy': 1.9446859375}
store['active_learning_steps'][0]['acquisition']={'indices': [42678, 570, 8586, 51314, 4873, 7979, 31341, 47322, 14817, 41478], 'labels': [3, 2, 9, 0, 8, 8, 0, 8, 0, 2], 'scores': [1.2585938572883606, 1.228684663772583, 1.217887282371521, 1.2139356136322021, 1.176763892173767, 1.1752762198448181, 1.1518842577934265, 1.148362398147583, 1.144141674041748, 1.1435993313789368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9404785633087158})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.1701884269714355})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.4337539672851562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4481170177459717})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7057, 'crossentropy': 1.7193814453125}
store['active_learning_steps'][1]['acquisition']={'indices': [5062, 34786, 4901, 28750, 826, 58076, 11659, 9460, 24773, 42365], 'labels': [9, 9, 9, 9, 9, 9, 5, 6, 5, 8], 'scores': [1.0011008977890015, 0.9893392324447632, 0.9887717366218567, 0.9836937189102173, 0.9790955781936646, 0.9728164076805115, 0.9710270762443542, 0.9675111770629883, 0.9637743234634399, 0.9602319598197937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.010162591934204})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.4592185020446777})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.724290370941162})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.827298879623413})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6908, 'crossentropy': 1.8117515625}
store['active_learning_steps'][2]['acquisition']={'indices': [45845, 12514, 54805, 46260, 38615, 12391, 55643, 969, 13091, 49257], 'labels': [2, 2, 2, 7, 7, 7, 5, 7, 7, 7], 'scores': [0.9981625080108643, 0.9948431849479675, 0.9888386130332947, 0.9810348153114319, 0.9792885184288025, 0.9567243456840515, 0.9499402046203613, 0.9474227428436279, 0.9457970261573792, 0.9431889653205872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.7488974332809448})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9575563669204712})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.0680150985717773})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.4883742332458496})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7194, 'crossentropy': 1.59588046875}
store['active_learning_steps'][3]['acquisition']={'indices': [56732, 25357, 47146, 59380, 39700, 17784, 54483, 55696, 49332, 17324], 'labels': [5, 5, 5, 8, 5, 8, 5, 8, 8, 3], 'scores': [0.930770754814148, 0.9229356646537781, 0.9195832014083862, 0.9179496765136719, 0.9132559895515442, 0.9104453325271606, 0.9094334244728088, 0.9043281078338623, 0.9031464457511902, 0.9016628265380859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4593935012817383})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.556746482849121})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.7783381938934326})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.062800884246826})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.747, 'crossentropy': 1.35307626953125}
store['active_learning_steps'][4]['acquisition']={'indices': [56664, 41900, 47278, 43378, 17540, 36427, 41194, 49537, 20641, 19574], 'labels': [2, 2, 5, 7, 1, 3, 7, 2, 9, 7], 'scores': [0.9249484539031982, 0.9127365350723267, 0.9036955237388611, 0.8906815648078918, 0.8873071670532227, 0.8872116804122925, 0.8840001821517944, 0.8772634267807007, 0.8743610978126526, 0.8724645972251892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2022532224655151})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.5436885356903076})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.6860041618347168})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.595184326171875})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7511, 'crossentropy': 1.18932666015625}
store['active_learning_steps'][5]['acquisition']={'indices': [28199, 53156, 48509, 53989, 53316, 38688, 50910, 6574, 16756, 48096], 'labels': [3, 3, 8, 2, 5, 7, 7, -1, 7, 7], 'scores': [0.905203104019165, 0.8712155818939209, 0.8560799956321716, 0.8536880612373352, 0.8518352508544922, 0.8516485691070557, 0.849595844745636, 0.8458964228630066, 0.8453992605209351, 0.8442857265472412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.1574089527130127})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3724123239517212})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.4656479358673096})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.4906809329986572})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7677, 'crossentropy': 1.117405078125}
store['active_learning_steps'][6]['acquisition']={'indices': [7833, 13991, 38817, 20547, 28469, 40905, 28455, 59390, 8700, 58476], 'labels': [5, 5, 5, 5, 5, 5, 5, 2, 3, 2], 'scores': [0.8514650464057922, 0.8031402826309204, 0.7990037202835083, 0.7853590250015259, 0.7720692157745361, 0.7643158435821533, 0.7458820939064026, 0.7450623512268066, 0.7445793747901917, 0.7413047552108765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1967159509658813})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0787692070007324})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.167468547821045})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2285056114196777})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.330369472503662})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8022, 'crossentropy': 1.00788759765625}
store['active_learning_steps'][7]['acquisition']={'indices': [12986, 16219, 34758, 27113, 27335, 22824, 5842, 46126, 28040, 6171], 'labels': [5, 5, 8, 2, 4, 9, 1, 3, 5, 5], 'scores': [0.9527655839920044, 0.9259900450706482, 0.914645254611969, 0.9084462523460388, 0.9025858044624329, 0.8946194052696228, 0.8944984078407288, 0.8939296007156372, 0.8928906917572021, 0.8880687952041626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1753630638122559})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.058510661125183})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0441385507583618})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3204128742218018})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3271548748016357})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.4989726543426514})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8399, 'crossentropy': 0.93087802734375}
store['active_learning_steps'][8]['acquisition']={'indices': [2381, 5013, 34899, 12525, 50343, 42891, 16456, 5474, 35232, 52582], 'labels': [7, 2, 7, 4, 6, 2, 2, 8, 8, 2], 'scores': [1.046606421470642, 1.0239620804786682, 1.023513376712799, 1.0117637515068054, 1.000527262687683, 0.9918681383132935, 0.9885640144348145, 0.9828009009361267, 0.980695903301239, 0.9784755110740662]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.170452356338501})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9299249053001404})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9826133847236633})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.149625539779663})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0922458171844482})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 0.87135048828125}
store['active_learning_steps'][9]['acquisition']={'indices': [28412, 19942, 55390, 57728, 1674, 52169, 47789, 31090, 32126, 38898], 'labels': [0, 5, 6, 9, 9, 2, 6, 4, 4, 4], 'scores': [0.9289736747741699, 0.9101171493530273, 0.8868927955627441, 0.8617295622825623, 0.8576917052268982, 0.8528671860694885, 0.8479174971580505, 0.8348127007484436, 0.8257865905761719, 0.8221100568771362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0815777778625488})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.977357029914856})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0984644889831543})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0141346454620361})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3911359310150146})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8364, 'crossentropy': 0.8566111328125}
store['active_learning_steps'][10]['acquisition']={'indices': [42697, 41608, 55181, 11649, 11113, 11685, 8825, 12267, 37227, 54009], 'labels': [4, -1, 4, 4, 4, 4, 4, 4, 4, 4], 'scores': [0.9109644293785095, 0.8773842453956604, 0.8680884838104248, 0.8599816560745239, 0.8557606935501099, 0.8509793877601624, 0.8496720194816589, 0.8468888401985168, 0.8440720438957214, 0.8414775133132935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0459909439086914})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8513487577438354})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0208238363265991})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1339930295944214})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1166918277740479})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8499, 'crossentropy': 0.77805185546875}
store['active_learning_steps'][11]['acquisition']={'indices': [49767, 36704, 11711, 2633, 43478, 42774, 5063, 7437, 57972, 44423], 'labels': [9, 2, 2, 9, 9, 4, 9, 7, 4, 9], 'scores': [0.8454760909080505, 0.8059807419776917, 0.794955849647522, 0.790337324142456, 0.7812945246696472, 0.7801522016525269, 0.779735803604126, 0.7780267000198364, 0.7750052809715271, 0.7719523310661316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0046937465667725})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8297514915466309})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8932211399078369})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0109542608261108})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.086837649345398})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8693, 'crossentropy': 0.747056689453125}
store['active_learning_steps'][12]['acquisition']={'indices': [55612, 36744, 24462, 5687, 25920, 43833, 58560, 25384, 52133, 8691], 'labels': [9, 1, 2, 3, 2, 3, 0, 5, 0, 2], 'scores': [0.8124568462371826, 0.8034752607345581, 0.802261471748352, 0.7985345125198364, 0.789267361164093, 0.7835897207260132, 0.7831747531890869, 0.7824476361274719, 0.7821723222732544, 0.7797186374664307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.0331344604492188})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.879601001739502})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7781492471694946})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7786756157875061})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9541911482810974})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8833966255187988})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8769, 'crossentropy': 0.7291736328125}
store['active_learning_steps'][13]['acquisition']={'indices': [12790, 59289, 13827, 13548, 843, 26444, 31883, 31941, 42703, 2765], 'labels': [4, 1, 3, 4, 3, 1, 4, 4, 0, 0], 'scores': [0.9437847137451172, 0.9265389442443848, 0.9262415170669556, 0.9252464771270752, 0.9250902533531189, 0.9210073351860046, 0.9047757983207703, 0.9037854671478271, 0.8983040452003479, 0.8909941911697388]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0328304767608643})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7392836809158325})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7383517026901245})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7378475666046143})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7773499488830566})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8925875425338745})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7720171213150024})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8909, 'crossentropy': 0.6974349609375}
store['active_learning_steps'][14]['acquisition']={'indices': [2148, 19356, 46524, 43043, 12236, 17404, 30441, 24616, 43126, 4955], 'labels': [6, 6, 6, 3, 1, 3, 1, 6, 3, 2], 'scores': [1.0771241784095764, 1.0403663516044617, 1.0354609489440918, 1.03452068567276, 1.0269961953163147, 1.0176527500152588, 1.0133740305900574, 1.0089530944824219, 1.0018886923789978, 0.9980449080467224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.012998104095459})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.705416202545166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7169530987739563})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7541386485099792})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6732110977172852})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6749078631401062})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7853687405586243})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7869264483451843})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.645838134765625}
store['active_learning_steps'][15]['acquisition']={'indices': [17129, 49517, 59303, 30123, 32519, 59314, 9118, 41426, 38050, 54932], 'labels': [1, 6, 8, 0, 5, 9, 9, 4, 6, 5], 'scores': [1.1018383502960205, 1.0713582634925842, 1.0407910346984863, 1.0359140038490295, 1.0344197750091553, 1.0297595858573914, 1.0230239629745483, 1.0119174718856812, 1.0090612173080444, 1.003776729106903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0738682746887207})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7032600045204163})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7141512632369995})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7446339130401611})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7014224529266357})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7357419729232788})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7428431510925293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7226388454437256})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.659236474609375}
store['active_learning_steps'][16]['acquisition']={'indices': [24457, 54401, 23890, 41933, 57371, 40702, 29132, 43745, 31273, 42139], 'labels': [8, -1, -1, 5, -1, 4, 8, 8, 8, 4], 'scores': [1.0598918795585632, 1.055057406425476, 1.0464231371879578, 1.0329259634017944, 1.0145589113235474, 1.0013081431388855, 0.9952115416526794, 0.9889934062957764, 0.9859063625335693, 0.9804775714874268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.910476565361023})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6531379818916321})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5906856060028076})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5773178339004517})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5926790237426758})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6101722717285156})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7136988043785095})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.559301171875}
store['active_learning_steps'][17]['acquisition']={'indices': [34743, 43823, 39355, 36818, 9555, 19948, 43000, 42209, 6272, 14733], 'labels': [9, 8, 8, 7, 9, 8, 9, 9, 9, 8], 'scores': [1.0442036390304565, 1.022027611732483, 1.0059941411018372, 1.0036541819572449, 0.9974473714828491, 0.9934951663017273, 0.9807833433151245, 0.9669522643089294, 0.9558317065238953, 0.9547690153121948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1075329780578613})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6371061205863953})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5605117082595825})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5467396974563599})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5282278060913086})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5502299666404724})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.551166296005249})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5945680737495422})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.481436083984375}
store['active_learning_steps'][18]['acquisition']={'indices': [5175, 49890, 5155, 54401, 49039, 1518, 2803, 19495, 4822, 37519], 'labels': [4, 5, 4, -1, -1, 9, 3, 3, 4, -1], 'scores': [1.036247193813324, 1.0270205736160278, 1.0244032144546509, 0.9938879013061523, 0.9900410175323486, 0.9862046241760254, 0.9823983311653137, 0.9674056172370911, 0.9646778702735901, 0.9635241627693176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0101490020751953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5928606986999512})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5624561309814453})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5896881818771362})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.547643780708313})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6138757467269897})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.614788293838501})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6151467561721802})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.49671103515625}
store['active_learning_steps'][19]['acquisition']={'indices': [49064, 45409, 17079, 37403, 39864, 49204, 32427, 38198, 7281, 20285], 'labels': [8, -1, 6, 2, 8, 9, 0, 0, 0, -1], 'scores': [1.0182704329490662, 1.0022883415222168, 0.9906538724899292, 0.9729812145233154, 0.964104175567627, 0.9632372856140137, 0.9628530740737915, 0.960332989692688, 0.9525075554847717, 0.9466474652290344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.050496220588684})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5637835264205933})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6071211695671082})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5557517409324646})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.505523681640625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.520291268825531})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5699512362480164})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5336212515830994})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.416238134765625}
store['active_learning_steps'][20]['acquisition']={'indices': [26472, 32776, 7759, 30585, 52140, 3486, 55128, 5679, 26270, 43648], 'labels': [-1, 4, -1, -1, 4, -1, 8, 3, -1, 5], 'scores': [1.0180919170379639, 1.0049906969070435, 0.971488356590271, 0.9686954021453857, 0.9633270502090454, 0.957560658454895, 0.9532945156097412, 0.9458391070365906, 0.9425091743469238, 0.941364049911499]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9535291790962219})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6168875694274902})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5532345175743103})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5223836898803711})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5172576904296875})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5428777933120728})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5159555673599243})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5735106468200684})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.570387601852417})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7243036031723022})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.4367294921875}
store['active_learning_steps'][21]['acquisition']={'indices': [53124, 11911, 43778, 49987, 20190, 25803, 30900, 14746, 15450, 14691], 'labels': [0, 0, 0, 0, 5, 0, 5, 0, 6, 3], 'scores': [1.0875588059425354, 1.0724599957466125, 1.0466750860214233, 1.040548324584961, 1.0399959087371826, 1.033724308013916, 1.0311792492866516, 1.0307921767234802, 1.030454695224762, 1.0246049165725708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0454041957855225})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5321945548057556})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45535558462142944})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4541056156158447})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5048103332519531})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5934621691703796})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4915505647659302})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.4069844970703125}
store['active_learning_steps'][22]['acquisition']={'indices': [40654, 46368, 52012, 9221, 34328, 32863, 7924, 37078, 45409, 6152], 'labels': [5, 8, 8, 1, 8, -1, 8, 8, -1, 8], 'scores': [0.9744009375572205, 0.9499990344047546, 0.945982813835144, 0.938700258731842, 0.9380896091461182, 0.9334348440170288, 0.9307349920272827, 0.9222416877746582, 0.9216585755348206, 0.9214685559272766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.021841049194336})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.605056643486023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4566551446914673})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46453186869621277})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4397498369216919})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4517239034175873})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.514427661895752})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5457730293273926})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9474, 'crossentropy': 0.365787255859375}
store['active_learning_steps'][23]['acquisition']={'indices': [43950, 47220, 32668, 42438, 53872, 38698, 18398, 49656, 14201, 7949], 'labels': [9, 6, 9, 9, 8, 5, 4, 9, 7, -1], 'scores': [0.98081374168396, 0.9473906755447388, 0.9431295990943909, 0.9409845471382141, 0.9278554320335388, 0.9211524724960327, 0.9016867280006409, 0.9001300930976868, 0.8931053876876831, 0.8904049396514893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1099257469177246})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5756558179855347})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5714341402053833})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48528921604156494})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.517116129398346})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5116931796073914})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48048585653305054})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5083932876586914})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47009676694869995})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.530943751335144})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5539069175720215})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5688170194625854})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9437, 'crossentropy': 0.437434130859375}
store['active_learning_steps'][24]['acquisition']={'indices': [28536, 28633, 59726, 18487, 54652, 8932, 24943, 16698, 35401, 50090], 'labels': [3, 3, 5, 4, -1, 0, 3, 5, 3, 4], 'scores': [1.1366639137268066, 1.1080619096755981, 1.1003059148788452, 1.098254382610321, 1.0724658966064453, 1.0620650053024292, 1.057830810546875, 1.0498583316802979, 1.0495645999908447, 1.039455771446228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1170117855072021})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6719530820846558})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4901599884033203})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4716883897781372})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4615707993507385})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5381092429161072})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6066082119941711})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6179802417755127})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9417, 'crossentropy': 0.419877197265625}
store['active_learning_steps'][25]['acquisition']={'indices': [22188, 37672, 22053, 16637, 10014, 43852, 50618, 26079, 50421, 11292], 'labels': [2, 8, 5, 8, 7, 2, 6, 8, 8, 1], 'scores': [1.005021095275879, 0.9770330786705017, 0.9737496972084045, 0.9688743948936462, 0.9446011185646057, 0.9273383617401123, 0.9222972989082336, 0.9208815097808838, 0.9179764986038208, 0.9163923263549805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1588236093521118})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6433458924293518})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4332318902015686})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4348089396953583})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45237308740615845})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5308064818382263})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.439064599609375}
store['active_learning_steps'][26]['acquisition']={'indices': [37962, 16951, 59747, 21636, 14749, 51464, 14649, 14558, 15945, 1239], 'labels': [8, 8, 5, 2, 0, 0, 0, 3, 3, 8], 'scores': [0.8725888133049011, 0.833968997001648, 0.8262340426445007, 0.8228881359100342, 0.8228020071983337, 0.8120443820953369, 0.8051754832267761, 0.8039829134941101, 0.7969121932983398, 0.7949897646903992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1392226219177246})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6408020257949829})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47610217332839966})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43276363611221313})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42208510637283325})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4122077524662018})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4337409734725952})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4135068953037262})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46188339591026306})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9516, 'crossentropy': 0.3803826904296875}
store['active_learning_steps'][27]['acquisition']={'indices': [5536, 20217, 22272, 3251, 52889, 50317, 137, 18307, 36990, 5408], 'labels': [8, 8, 5, 8, -1, 3, 8, -1, -1, 3], 'scores': [0.9906373023986816, 0.9821828603744507, 0.9767335653305054, 0.971293032169342, 0.9687458276748657, 0.9675110578536987, 0.9598917961120605, 0.9524387121200562, 0.9470551013946533, 0.9466238021850586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1489386558532715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5616012811660767})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47104611992836})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3869178295135498})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4278212785720825})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4581264853477478})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4290022552013397})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.350974072265625}
store['active_learning_steps'][28]['acquisition']={'indices': [52462, 27429, 4860, 26850, 57718, 28930, 21880, 30359, 42028, 56914], 'labels': [9, 0, 8, 2, 7, 7, 2, 7, 1, 0], 'scores': [0.8398400545120239, 0.8161126971244812, 0.8130040764808655, 0.8068812489509583, 0.7998905181884766, 0.7868096828460693, 0.7848451137542725, 0.784463107585907, 0.7819838523864746, 0.7803595066070557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2394901514053345})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6209635734558105})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45736128091812134})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33320754766464233})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.362064003944397})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3310618996620178})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36787551641464233})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37107768654823303})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33675384521484375})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3479035400390625}
store['active_learning_steps'][29]['acquisition']={'indices': [45616, 48681, 14305, 18193, 6347, 8463, 45954, 54195, 52358, 45800], 'labels': [5, 2, 8, -1, 3, 7, 8, 8, 2, 9], 'scores': [0.9868112802505493, 0.9778347015380859, 0.9560549259185791, 0.9440857172012329, 0.9438846111297607, 0.9374344944953918, 0.9351142048835754, 0.9301093816757202, 0.9296036958694458, 0.9248203635215759]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2180047035217285})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5788167715072632})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43714696168899536})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3952687382698059})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37777653336524963})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3832799196243286})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4271955192089081})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4141445755958557})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.392741943359375}
store['active_learning_steps'][30]['acquisition']={'indices': [20903, 18066, 14655, 15855, 38133, 51764, 31184, 1075, 49616, 1157], 'labels': [3, 7, 3, 5, 7, 5, 9, 7, 7, 7], 'scores': [0.8696730732917786, 0.8504935503005981, 0.847676157951355, 0.8410782217979431, 0.840046226978302, 0.8336147665977478, 0.83270263671875, 0.8324446082115173, 0.8313542008399963, 0.8303068280220032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.216653823852539})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6241834163665771})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4618068039417267})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41076433658599854})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3789461851119995})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39125382900238037})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47906380891799927})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3861607313156128})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9594, 'crossentropy': 0.342845556640625}
store['active_learning_steps'][31]['acquisition']={'indices': [14843, 37048, 54880, 31664, 49541, 45602, 34716, 12702, 7192, 7949], 'labels': [9, 9, 5, 3, 9, 5, 3, 3, 3, -1], 'scores': [0.9230215549468994, 0.9021314978599548, 0.9008159339427948, 0.8924503326416016, 0.8882075548171997, 0.8874234259128571, 0.8831431865692139, 0.8602749109268188, 0.8579442501068115, 0.8494579792022705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.392484426498413})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6645514369010925})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4289523959159851})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4021296203136444})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37336575984954834})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3961472809314728})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34710726141929626})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3440206050872803})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35768938064575195})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3749082684516907})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3849886655807495})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.3128684814453125}
store['active_learning_steps'][32]['acquisition']={'indices': [24479, 34520, 42334, 4185, 42673, 3691, 43702, 15723, 17494, 25868], 'labels': [8, 6, 5, 2, -1, 0, 3, 8, 5, -1], 'scores': [0.9707092642784119, 0.9667738676071167, 0.9457847476005554, 0.9433456063270569, 0.9390729069709778, 0.9326372146606445, 0.9286145567893982, 0.925449550151825, 0.9216219782829285, 0.9042294025421143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2463265657424927})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6547386646270752})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.44378945231437683})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38518935441970825})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3499095141887665})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35724449157714844})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3036344647407532})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.340626984834671})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29990699887275696})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34374645352363586})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3194930851459503})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3830123543739319})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.32341220703125}
store['active_learning_steps'][33]['acquisition']={'indices': [30884, 52889, 56512, 2782, 46995, 6066, 42673, 14210, 19081, 4036], 'labels': [2, -1, -1, -1, -1, 8, -1, -1, -1, -1], 'scores': [1.0600369572639465, 1.0425036549568176, 1.0407589673995972, 1.0223867893218994, 1.0094220042228699, 0.9963222742080688, 0.9891213178634644, 0.987866222858429, 0.9795570373535156, 0.9723181128501892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.2513604164123535})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6342452764511108})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4879605770111084})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37536317110061646})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3727956712245941})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3547486960887909})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3528364598751068})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.35110795497894287})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3351312279701233})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.3114872872829437})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3385172486305237})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3626915216445923})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3854677677154541})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.32116591796875}
store['active_learning_steps'][34]['acquisition']={'indices': [47927, 15948, 22728, 19078, 5740, 37450, 8228, 54652, 36421, 18348], 'labels': [-1, 2, -1, -1, 9, 4, 3, -1, 3, 8], 'scores': [1.0763685703277588, 1.0738593339920044, 1.051043689250946, 1.0492647886276245, 1.03880113363266, 1.025689959526062, 1.022571325302124, 1.0225567817687988, 1.0156067609786987, 1.0026851892471313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2762938737869263})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.627449631690979})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.44061657786369324})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3657667338848114})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.34028980135917664})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.364809513092041})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3263366222381592})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32981812953948975})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.326728880405426})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3593822717666626})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.311451318359375}
store['active_learning_steps'][35]['acquisition']={'indices': [47626, 29501, 50736, 25624, 34847, 19078, 51744, 19031, 45065, 22098], 'labels': [-1, -1, -1, -1, 0, -1, -1, 2, -1, -1], 'scores': [1.0173120498657227, 1.0049645900726318, 0.976983904838562, 0.9584982991218567, 0.951095461845398, 0.9461824893951416, 0.945809006690979, 0.9449104070663452, 0.9406945109367371, 0.9328889846801758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.334380865097046})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6717413663864136})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.43537476658821106})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4012768566608429})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3454855680465698})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35144472122192383})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.357318639755249})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3874111771583557})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.329540625}
store['active_learning_steps'][36]['acquisition']={'indices': [5974, 45409, 59378, 4036, 2782, 22728, 14722, 46995, 58134, 45065], 'labels': [-1, -1, -1, -1, -1, -1, 0, -1, -1, -1], 'scores': [1.041757583618164, 0.9915248155593872, 0.9861191511154175, 0.9838621616363525, 0.9677971005439758, 0.9545841217041016, 0.9050584435462952, 0.9047335386276245, 0.8979760408401489, 0.8770387172698975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1656458377838135})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6269562840461731})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4462481141090393})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4164386987686157})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3643167018890381})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3637760579586029})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34746888279914856})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3874717056751251})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3947160840034485})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4099845886230469})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.3161869384765625}
store['active_learning_steps'][37]['acquisition']={'indices': [20169, 42472, 7949, 38920, 19590, 55778, 43198, 47626, 33812, 24990], 'labels': [4, 2, -1, 7, 5, -1, 3, -1, 6, 7], 'scores': [1.0031818747520447, 0.9985073208808899, 0.9720662236213684, 0.9407061338424683, 0.9266273379325867, 0.9262063503265381, 0.9204127192497253, 0.9198229312896729, 0.9144831895828247, 0.906336784362793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.261905312538147})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7403253316879272})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5103570818901062})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4412207007408142})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40548017621040344})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3537684679031372})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34901249408721924})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36072641611099243})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34124019742012024})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3697212338447571})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3409000635147095})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3662409782409668})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35844022035598755})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34544017910957336})
store['active_learning_steps'][38]['training']['best_epoch']=11
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3292541748046875}
store['active_learning_steps'][38]['acquisition']={'indices': [32880, 44927, 13259, 32276, 15510, 47479, 22034, 39668, 7168, 55906], 'labels': [0, 7, 1, 3, 2, 0, 4, 8, 8, 2], 'scores': [1.0534087419509888, 0.9925450086593628, 0.9636086821556091, 0.9609594941139221, 0.9608448147773743, 0.9591342806816101, 0.9513804614543915, 0.9472430944442749, 0.9471048712730408, 0.9461600184440613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3226265907287598})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6794614791870117})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5298518538475037})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4334367513656616})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33442461490631104})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39476969838142395})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4036802053451538})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.37263554334640503})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9595, 'crossentropy': 0.3515177978515625}
store['active_learning_steps'][39]['acquisition']={'indices': [26358, 14337, 30444, 35864, 23956, 47626, 14256, 15913, 56662, 29851], 'labels': [3, 7, 6, 5, 4, -1, 6, 9, 0, -1], 'scores': [0.8748341798782349, 0.8253845572471619, 0.822736918926239, 0.8223863244056702, 0.8192945122718811, 0.8109654188156128, 0.8023918271064758, 0.7960147857666016, 0.7953473925590515, 0.7897564172744751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2833908796310425})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7205235362052917})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4665493369102478})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38868314027786255})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35832542181015015})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3615102469921112})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3547229766845703})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34448152780532837})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3590816259384155})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39225733280181885})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35036659240722656})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.325060791015625}
store['active_learning_steps'][40]['acquisition']={'indices': [36337, 48587, 46441, 44364, 50916, 37315, 15832, 17382, 40589, 12699], 'labels': [3, 3, 6, 2, 4, 6, 9, 6, 2, 6], 'scores': [0.9534797072410583, 0.9349465370178223, 0.9239045977592468, 0.9177300333976746, 0.9134686589241028, 0.908137321472168, 0.9077984094619751, 0.905511200428009, 0.8949722647666931, 0.8889028429985046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2426948547363281})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6270980834960938})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.4088360667228699})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.35253238677978516})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35913097858428955})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3217090964317322})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.35597506165504456})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3384566605091095})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.328673392534256})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.3104898193359375}
store['active_learning_steps'][41]['acquisition']={'indices': [27503, 47626, 48102, 11298, 5790, 59731, 48360, 38623, 16836, 22994], 'labels': [2, -1, 7, 2, 2, 5, 3, 8, 7, 2], 'scores': [0.9028186202049255, 0.857347846031189, 0.8487585186958313, 0.8380906283855438, 0.8323289752006531, 0.8295474052429199, 0.821159839630127, 0.8136321902275085, 0.8108963966369629, 0.8107337355613708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.351802110671997})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6430054903030396})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5071811079978943})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.38097885251045227})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3341329097747803})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36257293820381165})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34418928623199463})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35018646717071533})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.3060063232421875}
store['active_learning_steps'][42]['acquisition']={'indices': [47626, 52889, 53054, 28368, 18598, 26805, 22169, 42828, 31014, 7726], 'labels': [-1, -1, -1, 9, 9, -1, 2, 7, -1, 4], 'scores': [0.9649845361709595, 0.9540640711784363, 0.8850849270820618, 0.8822279572486877, 0.8735836148262024, 0.8696523904800415, 0.8511284589767456, 0.8303698301315308, 0.8256791830062866, 0.8178365230560303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3285465240478516})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.7276650071144104})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4877651333808899})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35035818815231323})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3588327467441559})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3564181327819824})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32767361402511597})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3406025767326355})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34471678733825684})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3371739387512207})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2966119140625}
store['active_learning_steps'][43]['acquisition']={'indices': [11616, 50736, 12066, 45520, 32909, 15701, 25634, 37347, 28030, 53054], 'labels': [7, -1, 8, 8, 9, 3, 9, 2, 0, -1], 'scores': [0.9790126085281372, 0.9439276456832886, 0.9046295881271362, 0.8991720676422119, 0.8932585716247559, 0.8884199857711792, 0.8880833387374878, 0.8805935978889465, 0.8797916769981384, 0.8776057958602905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4239217042922974})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7307239770889282})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5017343759536743})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.420019268989563})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3869069516658783})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3520861268043518})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36261749267578125})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.32951128482818604})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34041649103164673})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.35461580753326416})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.35556185245513916})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.315008154296875}
store['active_learning_steps'][44]['acquisition']={'indices': [14896, 13156, 7949, 9661, 47626, 35269, 39645, 48323, 45171, 23642], 'labels': [8, 2, -1, 8, -1, -1, -1, 2, -1, 2], 'scores': [1.0149832367897034, 1.0049130320549011, 0.987594723701477, 0.9743809103965759, 0.9496828317642212, 0.938957929611206, 0.9297850131988525, 0.926120400428772, 0.9259628653526306, 0.9215174913406372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3443269729614258})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.7143261432647705})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4762040078639984})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40509483218193054})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39394405484199524})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3088054060935974})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3675212264060974})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30648696422576904})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3426676392555237})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31198179721832275})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34916889667510986})
store['active_learning_steps'][45]['training']['best_epoch']=8
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.3038557373046875}
store['active_learning_steps'][45]['acquisition']={'indices': [7949, 32583, 24587, 24424, 1376, 6582, 13942, 9608, 1812, 13031], 'labels': [-1, -1, 8, 1, 7, 8, 4, 8, 4, 2], 'scores': [0.9445704817771912, 0.9060038328170776, 0.896378368139267, 0.8914934396743774, 0.8894563913345337, 0.8793699741363525, 0.8788726329803467, 0.8765813112258911, 0.8730911016464233, 0.8702328205108643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3676211833953857})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6397496461868286})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.45265665650367737})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4020858407020569})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40472155809402466})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33645176887512207})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2982236444950104})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3193991780281067})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3182447552680969})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3340790867805481})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.31026650390625}
store['active_learning_steps'][46]['acquisition']={'indices': [5298, 22481, 45666, 59701, 15781, 11074, 14144, 54858, 21287, 22497], 'labels': [0, 7, 1, 5, 5, 9, 5, 3, 4, 7], 'scores': [0.9188433885574341, 0.9179461002349854, 0.9067314863204956, 0.8689351677894592, 0.8660134077072144, 0.8621536493301392, 0.8576279878616333, 0.852287232875824, 0.847673773765564, 0.8424440622329712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.4124391078948975})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7178464531898499})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5572537183761597})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.45692741870880127})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3357585370540619})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35796815156936646})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.34024184942245483})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.3371119499206543})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.3312295166015625}
store['active_learning_steps'][47]['acquisition']={'indices': [46088, 33484, 51261, 51236, 3367, 1461, 34708, 45065, 30299, 26805], 'labels': [6, 6, 4, -1, 0, 4, 0, -1, 1, -1], 'scores': [0.8304505348205566, 0.8162588477134705, 0.7744897603988647, 0.773391604423523, 0.7690881490707397, 0.7684758901596069, 0.7683704495429993, 0.7662566900253296, 0.7611216902732849, 0.7530543804168701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3307113647460938})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5937037467956543})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5172966122627258})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4189707040786743})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3165602684020996})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32538795471191406})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31102898716926575})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2988422214984894})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3065541982650757})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.31137973070144653})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3259428143501282})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2949503662109375}
store['active_learning_steps'][48]['acquisition']={'indices': [8883, 57742, 47979, 12305, 49354, 8772, 18324, 6524, 51994, 32747], 'labels': [2, 6, 3, 9, 0, 1, 0, 5, 5, 8], 'scores': [0.9052178859710693, 0.8733357787132263, 0.8614293336868286, 0.848922073841095, 0.8454989790916443, 0.8413081765174866, 0.8394544124603271, 0.8298115730285645, 0.8243370056152344, 0.8235910534858704]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.31331205368042})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.7081432342529297})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4808673858642578})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39994579553604126})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3535693883895874})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.32529979944229126})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3209632635116577})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34160518646240234})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30354630947113037})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.34718838334083557})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.36085090041160583})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3528640866279602})
store['active_learning_steps'][49]['training']['best_epoch']=9
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.3230619384765625}
store['active_learning_steps'][49]['acquisition']={'indices': [23927, 25508, 21601, 49395, 23059, 49910, 5425, 52097, 7851, 47926], 'labels': [5, 5, 1, 1, 1, 6, 1, 1, 8, 8], 'scores': [0.9922993183135986, 0.9447186589241028, 0.9383065700531006, 0.9292507767677307, 0.9186594486236572, 0.915800929069519, 0.9022552967071533, 0.8866713047027588, 0.8865963220596313, 0.8836417198181152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.3132262229919434})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.644469141960144})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.458614706993103})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3946036696434021})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35026365518569946})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3052758276462555})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33295297622680664})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3300522565841675})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3058815002441406})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2955447998046875}
store['active_learning_steps'][50]['acquisition']={'indices': [31046, 18193, 52889, 29376, 7949, 50236, 20869, 3273, 38912, 29672], 'labels': [6, -1, -1, -1, -1, 0, 3, 8, -1, 9], 'scores': [0.8720752000808716, 0.8433667421340942, 0.8379806280136108, 0.8311271071434021, 0.8233085870742798, 0.810352087020874, 0.8005397915840149, 0.7984812259674072, 0.7937133312225342, 0.7902353405952454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4586948156356812})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6914335489273071})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5367804765701294})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.4429450035095215})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34783899784088135})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.35714083909988403})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3409404158592224})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31665581464767456})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3427320718765259})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2961411476135254})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33426913619041443})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3286038637161255})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3070710599422455})
store['active_learning_steps'][51]['training']['best_epoch']=10
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.272734423828125}
store['active_learning_steps'][51]['acquisition']={'indices': [52590, 32047, 52889, 2782, 623, 22550, 36761, 46995, 12651, 55043], 'labels': [-1, 9, -1, -1, 6, 6, -1, -1, 9, -1], 'scores': [0.9189364910125732, 0.914218544960022, 0.9070205688476562, 0.9062615036964417, 0.9054455161094666, 0.904373049736023, 0.8902444839477539, 0.8889838457107544, 0.8886786699295044, 0.8847489356994629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.252753734588623})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6989913582801819})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4539075493812561})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41034525632858276})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35996508598327637})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3085794448852539})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35157299041748047})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29328951239585876})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.301621675491333})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3373112678527832})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27040034532546997})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26851969957351685})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3023959994316101})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3187207579612732})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28507179021835327})
store['active_learning_steps'][52]['training']['best_epoch']=12
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.297005908203125}
