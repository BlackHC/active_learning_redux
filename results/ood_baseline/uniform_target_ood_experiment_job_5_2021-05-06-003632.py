store = {}
store['timestamp']=1620257792
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=5']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=5
store['worker_id']=5
store['num_workers']=40
store['config']={'seed': 6, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1609513759613037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.5409998893737793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.603879928588867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8016676902770996})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6702, 'crossentropy': 1.979759765625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 2381], ['id', 13823], ['id', 54345], ['ood', 18971], ['id', 39119], ['id', 5079], ['id', 10044], ['id', 13464], ['id', 81], ['id', 5192]], 'labels': [7, 4, 6, 2, 0, 5, 6, 0, 0, 0], 'scores': [0.7426685690879822, 0.5328590273857117, 0.7305967211723328, 0.7604588270187378, 1.1347562074661255, 0.8029441833496094, 1.0249775052070618, 1.043134331703186, 0.7960191965103149, 0.9765421152114868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.7257626056671143})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.036100387573242})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.1426010131835938})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.512460231781006})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7103, 'crossentropy': 1.5881587890625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 24093], ['id', 57447], ['id', 30833], ['id', 4164], ['id', 12555], ['id', 57902], ['id', 5991], ['id', 34287], ['id', 53332], ['id', 54493]], 'labels': [5, 8, 3, 7, 0, 5, 5, 2, 3, 3], 'scores': [0.7561768889427185, 0.6138858795166016, 0.7943874597549438, 0.5714110732078552, 0.7155227065086365, 0.6831516623497009, 0.6282564997673035, 0.8493728637695312, 0.8668652772903442, 0.760945737361908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4285144805908203})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.5761094093322754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.7983366250991821})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.1248602867126465})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7541, 'crossentropy': 1.283942578125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 4820], ['id', 23265], ['id', 20899], ['id', 57308], ['ood', 53873], ['ood', 6574], ['id', 7005], ['id', 10476], ['id', 22994], ['id', 57640]], 'labels': [5, 3, 1, 3, 8, 0, 2, 2, 2, 8], 'scores': [0.6065756678581238, 0.7432857751846313, 0.5386049747467041, 0.7388526201248169, 0.48913484811782837, 0.7487056255340576, 0.6203752160072327, 0.5536397695541382, 0.5483168959617615, 0.7084742784500122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1044292449951172})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.5175243616104126})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.5627025365829468})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.7147800922393799})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7802, 'crossentropy': 1.058262109375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27325], ['id', 38607], ['id', 42838], ['id', 54035], ['id', 27342], ['id', 23849], ['id', 826], ['id', 34231], ['id', 34971], ['id', 28708]], 'labels': [9, 7, 9, 7, 9, 7, 9, 7, 4, 6], 'scores': [0.4303230047225952, 0.6457747220993042, 0.5346477031707764, 0.5729860067367554, 0.33735018968582153, 0.6100718379020691, 0.5527467727661133, 0.4455088973045349, 0.4506211280822754, 0.32295680046081543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9770039319992065})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.10528564453125})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1322684288024902})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.098456859588623})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8201, 'crossentropy': 0.91527236328125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 31545], ['id', 18515], ['ood', 34180], ['id', 5606], ['id', 44901], ['id', 42210], ['id', 19505], ['id', 56047], ['id', 15261], ['id', 25499]], 'labels': [5, 0, 5, 5, 2, 3, 2, 3, 3, 6], 'scores': [0.7120242118835449, 0.4816718101501465, 0.45095646381378174, 0.5512874722480774, 0.5017417669296265, 0.409737765789032, 0.5028977394104004, 0.5949033498764038, 0.542320966720581, 0.5878349542617798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8787620663642883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.822291374206543})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8734050989151001})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9497522711753845})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0386035442352295})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8591, 'crossentropy': 0.809675537109375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 7871], ['id', 53064], ['id', 17011], ['id', 57462], ['id', 46316], ['id', 13682], ['id', 11211], ['id', 1350], ['id', 6305], ['id', 33110]], 'labels': [8, 8, 6, 5, 9, 8, 8, 6, 5, 1], 'scores': [0.6993274688720703, 0.47642719745635986, 0.6997652649879456, 0.5749220252037048, 0.5896174907684326, 0.7781444787979126, 0.631981372833252, 0.5659014582633972, 0.6843034029006958, 0.8405656814575195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.919125497341156})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8738751411437988})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8986231088638306})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9756270051002502})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.069199562072754})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8508, 'crossentropy': 0.826430078125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 31246], ['id', 35424], ['id', 2787], ['id', 13904], ['ood', 13062], ['id', 55522], ['id', 5673], ['id', 44389], ['id', 57736], ['id', 1448]], 'labels': [4, 6, 9, 9, 7, 4, 4, 1, 8, 4], 'scores': [0.5152662396430969, 0.7235425114631653, 0.564240574836731, 0.5354064702987671, 0.45460712909698486, 0.6463005542755127, 0.5637399554252625, 0.8070878982543945, 0.6303426623344421, 0.5795260667800903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8423592448234558})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7038816213607788})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7618545293807983})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7609330415725708})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8014880418777466})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.61536865234375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 30896], ['id', 15601], ['id', 15945], ['id', 16997], ['id', 24101], ['id', 45057], ['id', 41999], ['id', 2856], ['id', 7681], ['id', 813]], 'labels': [5, 9, 3, 0, 8, 8, 0, 4, 8, 2], 'scores': [0.5786152482032776, 0.7301909923553467, 0.6720951795578003, 0.4713349938392639, 0.7861109375953674, 0.6440563797950745, 0.47196346521377563, 0.6713039875030518, 0.7194277048110962, 0.5146408081054688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7247907519340515})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.634162187576294})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6446007490158081})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6415716409683228})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7644926309585571})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8956, 'crossentropy': 0.61120986328125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 23318], ['id', 52152], ['id', 24513], ['id', 48066], ['id', 47844], ['id', 41951], ['id', 47936], ['id', 36762], ['id', 16628], ['id', 27477]], 'labels': [1, 2, 2, 6, 7, 5, 8, 7, 9, 0], 'scores': [0.6118420362472534, 0.6764737963676453, 0.5436058640480042, 0.5088124871253967, 0.4631344676017761, 0.666233479976654, 0.7846590280532837, 0.72428297996521, 0.8557091951370239, 0.774435818195343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7972344160079956})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5748127102851868})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6429246664047241})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6714196801185608})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6727422475814819})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8993, 'crossentropy': 0.57376669921875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 2933], ['id', 43194], ['id', 16190], ['id', 46247], ['id', 4360], ['id', 21507], ['id', 53658], ['id', 40456], ['id', 59196], ['id', 21363]], 'labels': [5, 8, 3, 3, 6, 2, 2, 0, 5, 4], 'scores': [0.489050030708313, 0.6602837443351746, 0.7629284262657166, 0.6496855020523071, 0.6022793650627136, 0.8188607096672058, 0.5056717395782471, 0.7423073053359985, 0.6852454543113708, 0.536838173866272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.746448814868927})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5208709836006165})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.537074625492096})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5386090278625488})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5638072490692139})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.501474853515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 1129], ['id', 21353], ['id', 59951], ['id', 22404], ['id', 16379], ['id', 12017], ['id', 32537], ['id', 29206], ['id', 16019], ['id', 57716]], 'labels': [2, 0, 4, 3, 7, 3, 5, 4, 3, 2], 'scores': [0.6297007203102112, 0.7784329056739807, 0.4087510108947754, 0.607840359210968, 0.6292027235031128, 0.647560715675354, 0.5781571269035339, 0.5462590456008911, 0.6913877725601196, 0.5113654732704163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7425079345703125})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5350345373153687})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5564975738525391})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5323140621185303})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.536906898021698})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5705762505531311})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6064136028289795})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.48145087890625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 39383], ['id', 13626], ['id', 52697], ['id', 47741], ['id', 5045], ['id', 6636], ['id', 47497], ['id', 19590], ['id', 25308], ['id', 33222]], 'labels': [6, 8, 3, 5, 9, 5, 6, 5, 7, 5], 'scores': [0.6612901091575623, 0.7192280888557434, 0.8689876794815063, 0.8578959703445435, 0.6867698431015015, 0.8567156791687012, 0.6687343716621399, 0.7770669460296631, 0.5581113696098328, 0.8241419792175293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7256039977073669})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4647672772407532})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46957412362098694})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4431719481945038})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47322481870651245})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48519909381866455})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5671706795692444})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.444365576171875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 37363], ['id', 51544], ['id', 36422], ['ood', 27971], ['id', 13318], ['id', 29996], ['id', 30493], ['id', 36889], ['id', 8432], ['id', 17478]], 'labels': [8, 1, 1, 9, 6, 9, 1, 7, 8, 4], 'scores': [0.7629097700119019, 0.8902943730354309, 0.5729399919509888, 0.5066641569137573, 0.6233232021331787, 0.5487030148506165, 0.6820973753929138, 0.5213876366615295, 0.41188955307006836, 0.8703705072402954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7545551061630249})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5374866724014282})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4560803174972534})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4853876233100891})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49328166246414185})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5078303217887878})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9351, 'crossentropy': 0.438307666015625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37696], ['id', 14735], ['id', 36598], ['id', 22741], ['id', 41228], ['id', 3891], ['id', 52173], ['id', 47628], ['id', 42263], ['id', 9867]], 'labels': [2, 9, 8, 3, 0, 8, 7, 3, 4, 4], 'scores': [0.9222338795661926, 0.6812761425971985, 0.5854816436767578, 0.6884682178497314, 0.6340019702911377, 0.5658753514289856, 0.6703504323959351, 0.8382571339607239, 0.6508179903030396, 0.7232292294502258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7674505710601807})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48206883668899536})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4727907180786133})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42923134565353394})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44126880168914795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4247033894062042})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4340584874153137})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4863552153110504})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4502321481704712})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.3955183837890625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 51454], ['id', 1660], ['id', 8680], ['id', 39668], ['id', 3563], ['id', 47366], ['id', 12813], ['id', 52219], ['id', 19396], ['id', 50054]], 'labels': [4, 2, 8, 8, 5, 5, 7, 8, 5, 8], 'scores': [0.6974707841873169, 0.5047666430473328, 0.8140861392021179, 1.0019636750221252, 0.5106273889541626, 0.5149897038936615, 0.8046953082084656, 0.5351713299751282, 0.6759582757949829, 0.8947429656982422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8754570484161377})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5254452228546143})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4648401439189911})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4419364631175995})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4668545424938202})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.470537006855011})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41762399673461914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45854735374450684})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5107285380363464})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44117605686187744})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.944, 'crossentropy': 0.41546611328125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 48930], ['id', 19702], ['id', 17010], ['id', 49192], ['ood', 57836], ['id', 32391], ['id', 22491], ['ood', 49664], ['id', 9141], ['id', 17616]], 'labels': [3, 5, 3, 2, 0, 4, 2, 0, 3, 6], 'scores': [0.6450754404067993, 0.8528682589530945, 1.0845621824264526, 0.9252018332481384, 0.33535313606262207, 0.79583340883255, 0.634608268737793, 0.5086121559143066, 0.5749531388282776, 0.7596709728240967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8850995302200317})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5334876775741577})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.509518027305603})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4491150379180908})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43267732858657837})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4802033305168152})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4710233807563782})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5461679697036743})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9431, 'crossentropy': 0.3898414794921875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 38999], ['id', 50789], ['id', 42931], ['id', 54786], ['id', 53116], ['ood', 31260], ['id', 49563], ['id', 47076], ['id', 8443], ['id', 15874]], 'labels': [9, 1, 3, 1, 0, 2, 8, 8, 2, 5], 'scores': [0.5055250525474548, 0.7584196925163269, 0.7749900221824646, 0.5525132417678833, 0.8934734463691711, 0.41439199447631836, 0.8042923212051392, 0.7392278909683228, 0.7466980218887329, 0.6688342094421387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9520856142044067})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5388569831848145})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42170119285583496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3845950961112976})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3970341086387634})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42854487895965576})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37387219071388245})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42719876766204834})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42716184258461})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4131174385547638})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9526, 'crossentropy': 0.3759423828125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 32215], ['id', 41573], ['id', 1688], ['id', 32355], ['id', 47635], ['id', 4317], ['id', 59297], ['id', 48948], ['id', 49672], ['id', 23094]], 'labels': [7, 3, 6, 8, 8, 7, 1, 7, 5, 7], 'scores': [0.8322857618331909, 0.7977303266525269, 0.6357214748859406, 0.8603180050849915, 0.7798601388931274, 0.6616336107254028, 0.8814523816108704, 0.7079404890537262, 0.7874431610107422, 0.6420007348060608]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0084946155548096})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5192521810531616})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48587194085121155})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40682852268218994})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4355325698852539})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3889319896697998})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39154061675071716})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42897146940231323})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42795732617378235})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.353013134765625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 52717], ['id', 35246], ['id', 36072], ['id', 51722], ['id', 53522], ['id', 14604], ['id', 12425], ['id', 20641], ['ood', 703], ['ood', 163]], 'labels': [5, 8, 2, 4, 2, 6, 9, 9, 1, 1], 'scores': [0.4117196798324585, 0.7342658042907715, 1.023403525352478, 0.4943937063217163, 0.8341761827468872, 0.638390064239502, 0.6893024444580078, 0.9355350732803345, 0.43714332580566406, 0.5778204202651978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8918361663818359})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4623755216598511})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3946927785873413})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37045782804489136})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35928866267204285})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38865309953689575})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3693500757217407})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39170223474502563})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.311933935546875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 5175], ['id', 32774], ['id', 29530], ['id', 34739], ['id', 24630], ['id', 18096], ['id', 35128], ['id', 15068], ['id', 59747], ['id', 54978]], 'labels': [4, 8, 4, 9, 5, 6, 2, 1, 5, 2], 'scores': [0.6268038749694824, 0.5919450521469116, 0.5642787218093872, 0.7043349146842957, 0.6632143259048462, 0.5107446610927582, 0.6866680383682251, 0.5277456045150757, 0.8223904371261597, 0.37023913860321045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0330730676651})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5145607590675354})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4005289077758789})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39221489429473877})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3911059498786926})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39405059814453125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44075173139572144})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4281654953956604})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9533, 'crossentropy': 0.3367611328125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 37347], ['id', 45888], ['id', 56006], ['id', 34765], ['id', 26412], ['ood', 47952], ['id', 22964], ['id', 23538], ['id', 25828], ['id', 8867]], 'labels': [2, 9, 3, 6, 3, 0, 3, 4, 9, 8], 'scores': [0.6243100166320801, 0.6409217119216919, 0.6495991945266724, 0.6970745623111725, 0.9460137486457825, 0.519951581954956, 0.6069297194480896, 0.48467808961868286, 0.40186601877212524, 0.6480530500411987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9134105443954468})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5152447819709778})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39616554975509644})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4020405411720276})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40523335337638855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34941086173057556})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38889917731285095})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3815130591392517})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3845570981502533})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.316036572265625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 47322], ['id', 41180], ['id', 21700], ['id', 13760], ['id', 37450], ['id', 24311], ['id', 58832], ['id', 18150], ['id', 17265], ['id', 47962]], 'labels': [8, 8, 7, 6, 4, 8, 3, 8, 2, 6], 'scores': [0.7022834420204163, 0.6325291991233826, 0.7453219294548035, 0.7669185996055603, 0.8015797734260559, 0.6613397598266602, 0.7216004133224487, 0.6944527626037598, 0.6232612729072571, 0.5119406580924988]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.885980486869812})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4770791828632355})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38387149572372437})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3524215817451477})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35456955432891846})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37315452098846436})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3408716320991516})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3338788151741028})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3693045675754547})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3349720239639282})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.37118953466415405})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.3146719970703125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 22272], ['id', 27340], ['id', 52089], ['id', 3762], ['id', 51144], ['id', 27099], ['ood', 46724], ['id', 55054], ['id', 34740], ['id', 40589]], 'labels': [5, 5, 7, 8, 5, 5, 5, 3, 3, 2], 'scores': [1.075350821018219, 0.6931203007698059, 0.647318959236145, 0.7832555770874023, 0.9277284145355225, 0.6960106790065765, 0.40518903732299805, 0.8823250532150269, 0.8177319765090942, 0.8465874195098877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0955395698547363})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5382933616638184})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44362717866897583})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3756055235862732})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3396190404891968})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32198989391326904})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33829617500305176})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3622150719165802})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.353462278842926})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.3063148681640625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 37397], ['id', 47680], ['id', 16011], ['id', 41196], ['id', 22824], ['id', 20190], ['id', 26760], ['id', 49614], ['id', 49893], ['id', 2258]], 'labels': [3, 4, 5, 9, 9, 5, 8, 2, 3, 5], 'scores': [0.7719646096229553, 0.5160960555076599, 0.7746506035327911, 0.6599105596542358, 0.8278748393058777, 0.7082734704017639, 0.5721408128738403, 0.7093923091888428, 0.46099984645843506, 0.6632391214370728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9813557863235474})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.499247670173645})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3824448585510254})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3403547406196594})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.329828143119812})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3231307864189148})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3206377625465393})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30472248792648315})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34314125776290894})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3391525149345398})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3165074586868286})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.29753125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 45068], ['id', 720], ['id', 13742], ['id', 5602], ['id', 340], ['id', 15191], ['id', 10992], ['id', 788], ['id', 14413], ['id', 46368]], 'labels': [5, 8, 9, 2, 7, 0, 0, 9, 8, 8], 'scores': [0.5072021484375, 0.6599481701850891, 0.5714816153049469, 0.7259132862091064, 0.799578845500946, 0.9057761430740356, 0.749578595161438, 0.7190113663673401, 0.763971209526062, 0.7394363284111023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1021909713745117})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5430831909179688})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38954561948776245})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34960201382637024})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3240201473236084})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33465278148651123})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3151649832725525})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33929961919784546})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2770345211029053})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31262606382369995})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3469945192337036})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33172187209129333})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.2895341064453125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 45185], ['id', 7954], ['id', 49026], ['id', 30130], ['id', 32532], ['ood', 12939], ['id', 56695], ['id', 59918], ['id', 17958], ['id', 40732]], 'labels': [7, 0, 6, 3, 9, 5, 5, 0, 9, 0], 'scores': [0.7329304218292236, 0.7529377937316895, 0.7683902382850647, 0.9162338972091675, 0.5290722846984863, 0.5228557586669922, 0.894473671913147, 0.9396335482597351, 0.9721158146858215, 0.6671158671379089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.081817388534546})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5564632415771484})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.411493182182312})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3283805847167969})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33450666069984436})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30634328722953796})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30564743280410767})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2993306517601013})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2985995411872864})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.32071056962013245})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3126894235610962})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36117297410964966})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.308613671875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 50044], ['id', 26747], ['id', 22481], ['id', 35234], ['id', 39480], ['id', 19942], ['id', 53019], ['id', 56454], ['id', 49525], ['id', 36760]], 'labels': [8, 1, 7, 4, 9, 5, 2, 0, 8, 7], 'scores': [0.528263509273529, 0.6476449966430664, 0.770008385181427, 0.7387097477912903, 0.7773788571357727, 0.8688007593154907, 0.7160537242889404, 0.7912594676017761, 1.0198452472686768, 0.7942004799842834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9096534252166748})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5328792333602905})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34220677614212036})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3523539900779724})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.313340425491333})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31241172552108765})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30207425355911255})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30958929657936096})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32073846459388733})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3079109787940979})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.2801236328125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 22531], ['id', 41426], ['id', 46491], ['id', 33812], ['id', 23350], ['id', 16922], ['id', 34951], ['id', 47914], ['id', 11074], ['id', 7310]], 'labels': [4, 4, 6, 6, 8, 3, 7, 0, 9, 9], 'scores': [0.7566367983818054, 0.711807906627655, 0.5881617069244385, 0.9879097938537598, 0.8989459872245789, 0.6901535391807556, 0.6633570790290833, 0.8369596004486084, 0.7744280099868774, 0.2746666371822357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0947043895721436})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6195235252380371})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42594748735427856})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3630012571811676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3181239366531372})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3059055805206299})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3290320038795471})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31981152296066284})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34016096591949463})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.299902880859375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 12188], ['id', 27072], ['id', 32072], ['id', 9727], ['id', 16030], ['id', 5896], ['id', 25055], ['id', 31919], ['id', 28632], ['id', 52666]], 'labels': [7, 8, 8, 2, 2, 8, 3, 9, 7, 7], 'scores': [0.8805446624755859, 0.622257649898529, 0.469895601272583, 0.6491931080818176, 0.6305023431777954, 0.8033882975578308, 0.7435457706451416, 0.5979014039039612, 0.9022452235221863, 0.8335131406784058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.12042236328125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.646204948425293})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4080771505832672})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38391366600990295})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33959096670150757})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3513432741165161})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3135411739349365})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33639776706695557})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33043909072875977})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35083311796188354})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.2882107177734375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 45800], ['id', 53740], ['id', 38698], ['id', 35062], ['id', 52886], ['id', 29711], ['id', 57985], ['id', 32387], ['id', 12630], ['id', 45784]], 'labels': [9, 3, 5, 5, 7, 8, 4, 4, 8, 9], 'scores': [0.7632685899734497, 0.7706218361854553, 0.8762869238853455, 0.646570086479187, 0.6658480167388916, 0.9116630554199219, 0.8050934076309204, 0.812728762626648, 0.3979254961013794, 0.7041438221931458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1403543949127197})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5864648818969727})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43758726119995117})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37583523988723755})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3633047938346863})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3591720163822174})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32063695788383484})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3179931044578552})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3165168762207031})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3249031901359558})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35236138105392456})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3116392493247986})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3273279368877411})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.39296838641166687})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34614312648773193})
store['active_learning_steps'][30]['training']['best_epoch']=12
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.2836439697265625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 5684], ['id', 29922], ['id', 41229], ['id', 9384], ['id', 37360], ['id', 22320], ['id', 49064], ['id', 40944], ['id', 42415], ['ood', 53054]], 'labels': [6, 4, 3, 5, 2, 8, 8, 1, 7, 2], 'scores': [0.9057208299636841, 0.9237992763519287, 0.8140535950660706, 0.753902405500412, 0.9195818305015564, 0.8619436621665955, 0.9525927901268005, 0.7034815549850464, 0.7513271570205688, 0.7606653571128845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.101989984512329})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6152589321136475})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46164923906326294})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37235352396965027})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33920416235923767})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3188192546367645})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33153602480888367})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29090607166290283})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29631561040878296})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3223809599876404})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2901574373245239})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34650087356567383})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3508736789226532})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.324409544467926})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.271937451171875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 14756], ['id', 4955], ['id', 12651], ['id', 43478], ['id', 46126], ['id', 6540], ['id', 56590], ['id', 20169], ['id', 36314], ['id', 27966]], 'labels': [1, 2, 9, 9, 3, 2, 2, 4, 4, 9], 'scores': [0.6814185380935669, 0.8844949007034302, 0.8782694935798645, 0.788339763879776, 0.7868204712867737, 0.6485605537891388, 0.8651329278945923, 1.0676723718643188, 0.7407306432723999, 0.7183849811553955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2063195705413818})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6474920511245728})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.48275691270828247})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3368152379989624})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38379180431365967})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3081493675708771})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3120546042919159})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32984864711761475})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3404868245124817})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.3079961181640625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 6289], ['id', 34707], ['id', 16627], ['id', 2064], ['ood', 36892], ['id', 7732], ['id', 16799], ['id', 34442], ['ood', 27637], ['id', 17055]], 'labels': [2, 8, 2, 7, 5, 2, 9, 2, 7, 8], 'scores': [0.7661858797073364, 0.5819504857063293, 0.8374229669570923, 0.6261685788631439, 0.4195622205734253, 0.7098671197891235, 0.5937557816505432, 0.6473458409309387, 0.4855858087539673, 0.7500752806663513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1630699634552002})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7031214237213135})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47093504667282104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3912171721458435})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3359140157699585})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3239959478378296})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3363074064254761})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.337510347366333})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3224168121814728})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3130616545677185})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30622610449790955})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3350563049316406})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3395541310310364})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34406769275665283})
store['active_learning_steps'][33]['training']['best_epoch']=11
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.30932802734375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 36526], ['id', 21034], ['id', 56066], ['id', 37810], ['id', 3941], ['id', 32206], ['id', 56244], ['id', 58829], ['id', 17079], ['id', 42828]], 'labels': [9, 5, 7, 8, 3, 8, 4, 0, 6, 7], 'scores': [0.6721318066120148, 0.5859434008598328, 0.779071569442749, 0.66752028465271, 0.7026594281196594, 0.8288566470146179, 0.7903094291687012, 0.7686750888824463, 0.8321847915649414, 0.7573325634002686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.036144733428955})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5808337330818176})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39806926250457764})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3138980269432068})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30865103006362915})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34633731842041016})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3004481792449951})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.32019564509391785})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29083579778671265})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27422910928726196})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2812501788139343})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28072911500930786})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29233741760253906})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.260697216796875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 47828], ['id', 1598], ['id', 1682], ['id', 33708], ['id', 20792], ['id', 15680], ['id', 18247], ['id', 45954], ['id', 24426], ['id', 37758]], 'labels': [5, 8, 0, 4, 9, 2, 0, 8, 5, 0], 'scores': [0.5982376337051392, 0.5104290246963501, 0.6319314241409302, 0.4007644057273865, 0.9068965315818787, 0.692298948764801, 0.7655626535415649, 0.7756927013397217, 0.8574938774108887, 0.7877054810523987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2318437099456787})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5892484784126282})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4780552387237549})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38693368434906006})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3048044443130493})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3235681354999542})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2889261841773987})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2945130467414856})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2976849675178528})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3279936909675598})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.301919091796875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 9568], ['id', 23733], ['id', 28086], ['id', 52695], ['id', 14779], ['id', 17420], ['id', 56397], ['id', 35482], ['id', 1392], ['id', 39778]], 'labels': [5, 5, 4, 2, 8, 7, 0, 4, 7, 8], 'scores': [0.6753673553466797, 0.8254044651985168, 0.5970346927642822, 0.4276043176651001, 0.4841737747192383, 0.8340524435043335, 0.6512031555175781, 0.5242173075675964, 0.40805932879447937, 0.7693188190460205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.142111897468567})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5967922210693359})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48676925897598267})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36227765679359436})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35804587602615356})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2962518632411957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34776028990745544})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3015495538711548})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2989078760147095})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2782031494140625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 19089], ['id', 52169], ['id', 40064], ['id', 22169], ['id', 32880], ['id', 29759], ['id', 14305], ['id', 14637], ['id', 52225], ['id', 55314]], 'labels': [5, 2, 8, 2, 0, 5, 8, 4, 2, 6], 'scores': [0.7084153890609741, 0.9569797515869141, 0.4157627820968628, 0.6787935495376587, 0.716376006603241, 0.7185375094413757, 0.7052147388458252, 0.5074746608734131, 0.6510982513427734, 0.7745240926742554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.132009744644165})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6182458400726318})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42233806848526})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36102375388145447})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3111104667186737})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33699923753738403})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2886333465576172})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28688904643058777})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2912333607673645})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29696333408355713})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27390098571777344})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3046203851699829})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2653648853302002})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.306320458650589})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30970335006713867})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.309937059879303})
store['active_learning_steps'][37]['training']['best_epoch']=13
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2641107421875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 57794], ['id', 33948], ['id', 17234], ['id', 10982], ['id', 36109], ['id', 44927], ['id', 54038], ['id', 19866], ['id', 24933], ['id', 29352]], 'labels': [9, 9, 9, 1, 9, 7, 9, 3, 1, 3], 'scores': [0.36604058742523193, 0.4822191894054413, 0.6090774536132812, 0.7263174653053284, 0.9280098676681519, 0.6035645008087158, 0.552018940448761, 0.889601469039917, 0.41548973321914673, 0.5619402527809143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2962522506713867})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.665662944316864})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.44577664136886597})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3721862733364105})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3239957094192505})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27859222888946533})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26036423444747925})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29200953245162964})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2794778645038605})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27699095010757446})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2647017822265625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 27083], ['ood', 43948], ['id', 42078], ['id', 34660], ['id', 52738], ['id', 26444], ['id', 49217], ['id', 24108], ['id', 18720], ['id', 36152]], 'labels': [7, 7, 4, 3, 1, 1, 8, 8, 7, 7], 'scores': [0.5858500003814697, 0.39006710052490234, 0.8690376877784729, 0.6684065461158752, 0.510944664478302, 0.7606960535049438, 0.6840682029724121, 0.46178245544433594, 0.6642317771911621, 0.5714520215988159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1254016160964966})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6146469712257385})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4499529004096985})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38083702325820923})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30813273787498474})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3033834397792816})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28964173793792725})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.290790855884552})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2817239761352539})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29095810651779175})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2865918278694153})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3281112313270569})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2623428466796875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 15771], ['id', 1674], ['id', 56300], ['id', 48102], ['id', 57507], ['id', 6347], ['id', 42963], ['id', 57575], ['id', 32276], ['id', 37538]], 'labels': [5, 9, 9, 7, 0, 3, 9, 0, 3, 9], 'scores': [0.8812974095344543, 0.8723087906837463, 0.6525769829750061, 0.7267066836357117, 0.8463039398193359, 0.9524059295654297, 0.8321623206138611, 0.876732349395752, 0.7572547793388367, 0.6023515462875366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2385272979736328})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.67689049243927})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.470059871673584})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35056209564208984})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31868648529052734})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29995834827423096})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29926201701164246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30049929022789})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30904504656791687})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2713502049446106})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2561657130718231})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24977423250675201})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2786441147327423})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26488712430000305})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2622222900390625})
store['active_learning_steps'][40]['training']['best_epoch']=12
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9733, 'crossentropy': 0.2510516845703125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 7793], ['id', 50572], ['id', 15948], ['id', 20150], ['id', 45739], ['id', 49487], ['id', 17549], ['id', 25498], ['id', 38252], ['id', 227]], 'labels': [8, 1, 2, 3, 9, 8, 0, 4, 5, 9], 'scores': [0.8764206767082214, 0.7941223382949829, 0.8209219574928284, 0.6262238025665283, 0.8389531970024109, 0.7131345868110657, 0.797563910484314, 0.6439533233642578, 0.7244958877563477, 0.4993969798088074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.307136058807373})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6280711889266968})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44824206829071045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33504313230514526})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2888467311859131})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30071917176246643})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3062881529331207})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28387731313705444})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29501715302467346})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27392178773880005})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2873762249946594})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2811434268951416})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30198347568511963})
store['active_learning_steps'][41]['training']['best_epoch']=10
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.241098095703125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 29179], ['id', 21430], ['id', 1282], ['id', 39405], ['id', 49318], ['id', 13428], ['id', 34847], ['id', 24733], ['id', 42504], ['id', 440]], 'labels': [8, 4, 9, 5, 3, 9, 0, 3, 8, 0], 'scores': [0.528329610824585, 0.46500682830810547, 0.7245162129402161, 0.6193354725837708, 0.46988973021507263, 0.8903513550758362, 0.9035674929618835, 0.5375473499298096, 0.5923039019107819, 0.7609712779521942]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2370728254318237})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6204016208648682})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3913215100765228})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3599058985710144})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2670765221118927})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2798430919647217})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31541743874549866})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3188546895980835})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2854947021484375}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 55088], ['id', 28468], ['id', 41753], ['id', 42384], ['id', 28136], ['id', 23886], ['id', 36686], ['id', 19254], ['id', 54885], ['id', 43256]], 'labels': [7, 4, 3, 8, 8, 1, 6, 9, 6, 3], 'scores': [0.3939630389213562, 0.5522165298461914, 0.31949496269226074, 0.6913810968399048, 0.6233024597167969, 0.5884822607040405, 0.45626312494277954, 0.4751896858215332, 0.6971628665924072, 0.695252001285553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2117952108383179})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5880413055419922})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.49600645899772644})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36224013566970825})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32288819551467896})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30719059705734253})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29458338022232056})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.258963406085968})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2700748145580292})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25639817118644714})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3015681505203247})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28726279735565186})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25591209530830383})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2799246311187744})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28447645902633667})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26806965470314026})
store['active_learning_steps'][43]['training']['best_epoch']=13
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.975, 'crossentropy': 0.2285413330078125}
